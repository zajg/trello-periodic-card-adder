class Card:
    __cards_counter = 0

    def get_counter():
        return Card.__cards_counter
    get_counter = staticmethod(get_counter)

    def __init__(self, cards_title, cards_description, cards_labels, cards_members, board_address):
        self.__cards_title = cards_title
        self.__cards_description = cards_description
        self.__cards_labels = cards_labels
        self.__cards_members = cards_members
        self.__board_address = board_address
        Card.__cards_counter += 1

    def __del__(self):
        Card.__cards_counter -= 1

    def print_card(self):
        print \
            self.__cards_title + ' ' + \
            self.__cards_description + ' ' + \
            self.__cards_labels + ' ' + \
            self.__cards_members + ' ' + \
            self.__board_address

    def get_title(self):
        return self.__cards_title

    def get_description(self):
        return self.__cards_description

    def get_labels(self):
        return self.__cards_labels

    def get_members(self):
        return self.__cards_members

    def get_board(self):
        return self.__board_address

    def set_title(self, new_title):
        self.__cards_title = new_title

    def set_description(self, new_description):
        self.__cards_description = new_description

    def set_labels(self, new_labels):
        self.__cards_labels = new_labels

    def set_members(self, new_members):
        self.__cards_members = new_members

    def set_board(self, new_board):
        self.__board_address = new_board

