import os
import datetime
import time
from Board import Board


class Updater:
    def __init__(self, data):
        self.__data_path = data
        self.__boards = []
        self.__paused = False

    def start(self):
        if not self.__paused:
            print "[LOG] Performing update: " + str(datetime.datetime.now())
            self.__update()
            tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
            update_time = tomorrow.replace(hour=4, minute=0, second=0, microsecond=0)
            print "[LOG] Update finished. Next update: " + str(update_time)
            sleeptime = (update_time - datetime.datetime.now()).seconds
            time.sleep(sleeptime)

    def pause(self):
        self.__paused = True

    def resume(self):
        self.__paused = False

    def __update(self):
        del self.__boards[:]
        for file_name in os.listdir(self.__data_path):
            if "board" in file_name:
                self.__boards.append(Board(self.__data_path + "/" + file_name))
        for board in self.__boards:
            board.update()
        return

