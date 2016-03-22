import smtplib

CONFIG = "data/email.txt"


class CardAdder:
    def __init__(self):
        with open(CONFIG) as f:
            self.__username = f.readline()
            self.__password = f.readline()
            self.__smtp = f.readline()

    def __send(self, msg, board_address):
        server = smtplib.SMTP(self.__smtp)
        server.ehlo()
        server.starttls()
        server.login(self.__username, self.__password)
        server.sendmail(self.__username, board_address, msg)
        server.quit()
        return

    def add_card(self, card):
        msg = "\r\n".join([
            "Subject: "+card.get_title()+" "+card.get_labels() + " " + card.get_members(),
            "",
            card.get_description()
        ])
        self.__send(msg, card.get_board())
        return


