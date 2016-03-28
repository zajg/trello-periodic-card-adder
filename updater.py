import datetime
import time
from sheet import Sheet
import imaplib
import fileinput
import sys

SHEETS_FILE = 'sheets.txt'


class Updater:
    def __init__(self, data):
        self.__data_path = data
        self.__sheets = []
        self.__paused = False

    def start(self):
        if not self.__paused:
            print "[LOG] Performing update: " + str(datetime.datetime.now())
            Updater.__update_sheets()
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

    @staticmethod
    def __replace_in_file(file_path, search_exp, replace_exp):
        for line in fileinput.input(file_path, inplace=1):
            if search_exp in line:
                line = line.replace(search_exp, replace_exp)
            sys.stdout.write(line)

    @staticmethod
    def __get_list_of_emails():
        connection = imaplib.IMAP4_SSL('imap.gmail.com')
        connection.login('trello.sender@gmail.com', 't3]5h9^7f]^#E')
        connection.list()  # Out: list of "folders" aka labels in gmail.
        connection.select("inbox")  # connect to inbox.
        result, data = connection.search(None, "UNSEEN")
        return connection, data[0].split()  # ids is a space separated string

    @staticmethod
    def __add_to_file(subject):
        subject = subject[4:]
        sheets = open("data/sheets.txt", 'a+')
        sheets.write(subject + '\r\n')
        sheets.close()
        print 'Dodawanie: ' + subject

    @staticmethod
    def __remove_from_file(subject):
        subject = subject[7:]
        Updater.__replace_in_file('data/sheets.txt', subject + '\r\n', '')
        print 'Usuwanie: ' + subject

    @staticmethod
    def __get_subject(connection, email):
        data = connection.fetch(email, '(BODY[HEADER.FIELDS (SUBJECT)])')
        subject = data[1][0][1]
        return subject[9:-4]

    @staticmethod
    def __update_sheets():
        connection, emails_list = Updater.__get_list_of_emails()
        for email in emails_list:
            subject = Updater.__get_subject(connection, email)
            if subject.startswith('Add '):
                Updater.__add_to_file(subject)
            elif subject.startswith('Remove '):
                Updater.__remove_from_file(subject)

