import smtplib

CONFIG = "data/config.txt"


class CardAdder:
    def __init__(self, username, password, smtp, board_address):
        self.__username = username
        self.__password = password
        self.__smtp = smtp
        self.__board_address = board_address

    def __init__(self, board_address):
        with open(CONFIG) as f:
            self.__username = f.readline()
            self.__password = f.readline()
            self.__smtp = f.readline()
            self.__board_address = board_address

    def __send(self, msg):
        server = smtplib.SMTP(self.__smtp)
        server.ehlo()
        server.starttls()
        server.login(self.__username, self.__password)
        server.sendmail(self.__username, self.__board_address, msg)
        server.quit()
        return

    def add_card(self, card):
        msg = "\r\n".join([
            "Subject: "+card.get_title()+" "+card.get_labels(),
            "",
            card.get_description()
        ])
        self.__send(msg)
        return


