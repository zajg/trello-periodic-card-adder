import datetime
import time
from sheet import Sheet

SHEETS_FILE = 'sheets.txt'


class Updater:
    def __init__(self, data):
        self.__data_path = data
        self.__sheets = []
        self.__paused = False

    def start(self):
        if not self.__paused:
            print "[LOG] Performing update: " + str(datetime.datetime.now())
            self.__make_update()
            tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
            update_time = tomorrow.replace(hour=4, minute=0, second=0, microsecond=0)
            print "[LOG] Update finished. Next update: " + str(update_time)
            sleep_time = (update_time - datetime.datetime.now()).seconds
            time.sleep(sleep_time)

    def pause(self):
        self.__paused = True

    def resume(self):
        self.__paused = False

    def __make_update(self):
        with open(self.__data_path + "/" + SHEETS_FILE) as f:
            sheet_keys = f.read().splitlines()
        for sheet_key in sheet_keys:
            sheet = Sheet(sheet_key)
            sheet.update()
        return

