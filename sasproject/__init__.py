from .connection import *
from .process import *


def setup(config):
    print(config["author"])
    try:
        com = Arduino(config["xbee_port"], config["xbee_freq"], config["xbee_timeout"])
        db = Database(config["dbhost"], config["dbuser"], config["dbpass"], config["dbname"])
        while True:
            data_in = com.read()
            if data_in:
                print("[log] read : %s" % data_in)
                process_data = Process().decompose(data_in)
                db.cursor("SQL")

                pass

    except KeyboardInterrupt:
        print("")
    finally:
        print("script complete")
    pass
