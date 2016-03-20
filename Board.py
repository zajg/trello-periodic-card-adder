import datetime
from Card import Card
from CardAdder import CardAdder


class Board:
    def __init__(self, path):
        self.__path = path
        self.__board_address = ""
        self.__card_definitions = ""
        self.__cards = []

    def update(self):
        if self.__read_file():
            return 1
        if self.__create_cards_from_definitions() < 1:
            return 2
        self.__add_cards()
        return 0

    def __read_file(self):
        with open(self.__path) as f:
            self.__board_address = f.readline()
            self.__card_definitions = f.readlines()
        return self.__board_address == "" or self.__card_definitions == ""

    def __create_cards_from_definitions(self):
        del self.__cards[:]
        for definition in self.__card_definitions:
            args = definition.split(" @@@ ")
            day_param = args[1]
            date_from = datetime.datetime.strptime(args[2], '%d.%m.%Y')
            date_to = datetime.datetime.strptime(args[3], '%d.%m.%Y')
            if args[0] == 'e':
                if (datetime.datetime.now() - date_from).days % int(day_param) == 0 \
                        and date_to >= datetime.datetime.now() >= date_from:
                    self.__cards.append(Card(args[4], args[5], args[6]))
            elif args[0] == 'w':
                if datetime.datetime.now().weekday() == int(day_param)\
                        and date_to >= datetime.datetime.now() >= date_from:
                    self.__cards.append(Card(args[4], args[5], args[6]))
            elif args[0] == 'm':
                if datetime.datetime.now().day == int(day_param)\
                        and date_to >= datetime.datetime.now() >= date_from:
                    self.__cards.append(Card(args[4], args[5], args[6]))
        return len(self.__cards)

    def __add_cards(self):
        card_adder = CardAdder(self.__board_address)
        for card in self.__cards:
            card_adder.add_card(card)
        return
