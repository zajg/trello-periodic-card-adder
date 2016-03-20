class Card:
    __cards_counter = 0

    def get_counter():
        return Card.__cards_counter
    get_counter = staticmethod(get_counter)

    def __init__(self, cards_title, cards_description, cards_labels):
        self.__cards_title = cards_title
        self.__cards_description = cards_description
        self.__cards_labels = cards_labels
        Card.__cards_counter += 1

    def __del__(self):
        Card.__cards_counter -= 1

    def get_title(self):
        return self.__cards_title

    def get_description(self):
        return self.__cards_description

    def get_labels(self):
        return self.__cards_labels

    def set_title(self, new_title):
        self.__cards_title = new_title

    def set_description(self, new_description):
        self.__cards_description = new_description

    def set_labels(self, new_labels):
        self.__cards_labels = new_labels

