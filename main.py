""" Affordable Price Finder v0.1
    simple app that enables user
    searching for his/her dream house
    for renting in Ireland
    using www.daft.ie """

import PySimpleGUI as sg
import urllib.request
import local_settings 
import pandas as pd
from daftlistings import Daft, Location, SearchType, PropertyType, SortType, MapVisualization

def check_connection():
    status_code = urllib.request.urlopen(local_settings.DAFT_URL).getcode()

    if status_code == 200:
        on_or_404 = 'OK'
    else:
        on_or_404 = 'NOT OK'
    
    return on_or_404


conn = check_connection()

class Person():
    def __init__(self, name, where, price, action, kind):
        self.name = name
        self.where = where
        self.price = price
        self.action = action
        self.kind = kind

    def __str__(self):
        return self.name +', ' +self.where +', ' +self.price +' ' +self.action + ' ' +self.kind
    
    def change_price(self, value):
        value = self.price

""" Main Program Loop""" 

# Very basic form.  Return values as a list
form = sg.FlexForm('Dream House Finder')  # begin with a blank form

layout = [
            [sg.Text('Connection status:' +check_connection())],
            [sg.Text('Please enter your Name, Location and you monthy income')],
            [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
            [sg.Text('Location', size=(15, 1)), sg.InputCombo(('CORK_CITY', 'DUBLIN_CITY', 'GALWAY_CITY', 'LIMERICK_CITY'))],
            [sg.Text('Price', size=(15, 1)), sg.InputText('Enter your monthly salary')],
            [sg.Text('Buy or Rent', size=(15, 1)), sg.InputCombo(('RESIDENTIAL_RENT', 'RESIDENTIAL_SALE'))],
            [sg.Text('Property Type', size=(15, 1)), sg.InputCombo(('HOUSE', 'APARTMENT'))],
          [ sg.Submit(), sg.Cancel()]
         ]
# 

button, values = form.Layout(layout).Read()

user = Person(values[0], values[1], values[2], values[3], values[4])
print(button, values[0], values[1], values[2], values[3], values[4])

print(user)

# second window

form = sg.FlexForm('Welcome ' +user.name)  # begin with a blank form

layout = [
          [sg.Text('System is searching for your dream property')], 
          [sg.Text('Your monthly salary is ' +user.price)],
          [sg.Text('Your desired location is ' +user.where)],
          [sg.Text('You going for ' +user.action)],
          [sg.Text('Your property type ' +user.kind)],
          [sg.Cancel()]
         ]

button, values = form.Layout(layout).Read()
