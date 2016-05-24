from .connection import *
from .process import *
import time


def setup(config):
    """Docstring for setup
    init communication object and make the connection with the Arduino for read and write requirements.
    """
    print(config["name"] + "v:" + config["version"])
    print("made by %s <%s>" % (config["author"], config["author_email"]))
    try:
        # init Xbee communication
        com = Arduino(config["xbee_port"], config["xbee_freq"], config["xbee_timeout"])
        # init database connection
        db = Database(config["dbhost"], config["dbuser"], config["dbpass"], config["dbname"])
        # create data process object
        processing = Process()

        while True:
            # send a request for sensors data to the arduino.
            com.write("readData")
            time.sleep(0.5)
            # read data incoming from the arduino
            data_in = com.read()

            # if i got data ->
            if data_in:
                # Require en tableau
                required_sql = db.cursor("SELECT * from requirements ORDER BY idrequirements DESC LIMIT 1")
                # process the table in valuable data
                required_data = processing.readsql(required_sql)
                print("[log] read : %s" % data_in)
                # process the data from the arduino in valuable data
                process_data = Process().decompose(data_in)
                # converts those data in a sql request for make a save of the day
                sql = Process().setsql(process_data)
                # exec sql
                db.cursor(sql)
                # call the ai to choose any order for the arduino
                request = processing.core_choice(process_data, required_data)

                # if we need modifications ->
                if request:

                    # each order will be send one by one.
                    for row in request:

                        com.write(row)
                        pass

                    del request
                pass

            del data_in

    except KeyboardInterrupt:
        print('\n')
        print("keyboard interrupt.")
    finally:
        print("script ended.")

    pass
