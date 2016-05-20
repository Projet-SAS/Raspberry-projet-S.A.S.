from .connection import *
from .process import *
import time


def setup(config):
    print(config["author"])
    try:
        com = Arduino(config["xbee_port"], config["xbee_freq"], config["xbee_timeout"])
        db = Database(config["dbhost"], config["dbuser"], config["dbpass"], config["dbname"])
        while True:
            com.write("readData")
            data_in = com.read()
            time.sleep(1)
            if data_in:
                print("[log] read : %s" % data_in)
                process_data = Process().decompose(data_in)
                sql = Process().setsql(process_data)
                db.cursor(sql)
                pass

    except KeyboardInterrupt:
        print("")
    finally:
        print("script complete")

    pass
