import requests
import csv
from sheet import Sheet

key = "19bvUZLmM6PoXsL6gfUP3iEzrtnFcxxdvi-Ib2p3GAuc"

sheet = Sheet(key)
sheet.update()

#response = requests.get('https://docs.google.com/spreadsheets/d/' + key + '/export?gid=0&format=csv')
#print response.text

