import datetime
import requests
import csv
from card import Card
from cardadder import CardAdder


class Sheet:
    def __init__(self, key):
        self.__key = key

    def update(self):
        csv_file = self.__get_csv()
        if csv_file == 1:
            return 1
        card_list = self.__list_from_csv(csv_file)
        if len(card_list) == 0:
            return 1
        cards = self.__create_cards(card_list)
        if len(cards) == 0:
            return 1
        self.__add_cards(cards)
        return 0

    def __get_csv(self):
        # get csv file from google sheets
        response = requests.get('https://docs.google.com/spreadsheets/d/' + self.__key + '/export?gid=0&format=csv')
        if response.status_code == 200:
            return response.text
        else:
            return 1

    @staticmethod
    def __list_from_csv(text):
        # convert csv to list
        reader = csv.reader(text.splitlines())
        return list(reader)

    @staticmethod
    def __create_cards(card_list):
        # create cards from list elements
        cards = []
        for card in card_list[1:]:  # skip columns names
            if len(card) == 9:
                day_param = card[6]
                date_from = datetime.datetime.strptime(card[7], '%Y-%m-%d')
                date_to = datetime.datetime.strptime(card[8], '%Y-%m-%d')
                if 'every' in card[5]:
                    if (datetime.datetime.now() - date_from).days % int(day_param) == 0 \
                            and date_to >= datetime.datetime.now() >= date_from:
                        cards.append(Card(card[0], card[1], card[2], card[3], card[4]))
                elif 'week' in card[5]:
                    if datetime.datetime.now().weekday() == int(day_param)\
                            and date_to >= datetime.datetime.now() >= date_from:
                        cards.append(Card(card[0], card[1], card[2], card[3], card[4]))
                elif 'month' in card[5]:
                    if datetime.datetime.now().day == int(day_param)\
                            and date_to >= datetime.datetime.now() >= date_from:
                        cards.append(Card(card[0], card[1], card[2], card[3], card[4]))
        return cards

    @staticmethod
    def __add_cards(cards):
        card_adder = CardAdder()
        for card in cards:
            card_adder.add_card(card)
        return
