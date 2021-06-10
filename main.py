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
    """ func that checks connection to daft.ie """
    status_code = urllib.request.urlopen(local_settings.DAFT_URL).getcode()

    if status_code == 200:
        on_or_404 = 'OK'
    else:
        on_or_404 = 'NOT OK'
    
    return on_or_404


class Person():
    """ class that describes all info needed for app to work 
        name = Your Name
        where = What city you are looking for (CORK_CITY, LIMERICK_CITY, DUBLIN_CITY, GALWAY_CITY)
        price = your monthly salary
        action = are you looking buy or rent
        kind = HOUSE or APARTMENT
    """
    def __init__(self, name, where, price, action, kind):
        self.name = name
        self.where = where
        self.price = price
        self.action = action
        self.kind = kind

    def __str__(self):
        return self.name +', ' +self.where +', ' +self.action + ' ' +self.kind
    
    def change_price(self, value):
        """ function for further development to change desired salary """ 
        value = self.price

    def calc_price(self):
        """ function that uses algorithm to return amount
        that user is willing to spend on his house
        if user chose residential sale salary is multiplied by
        12 months and then utilizes 5times multiplier as bank take
        that value for mortage 
        """
        price = self.price
        action = self.action
        mortage = 5 # here set mortage multiplier 

        if action == 'RESIDENTIAL_SALE':
            return price * 12 * mortage


        if price >= 10000:
            return price * 0.7
        elif price < 10000 & price >= 5000:
            return price * 0.55
        elif price < 5000 & price >= 2800:
            return price * 0.475
        else:
            return price * 0.4


""" Main Program Loop""" 

fonts = local_settings.FONT_SMALL
# Very basic form.  Return values as a list
form = sg.FlexForm('Dream House Finder')  # begin with a blank form

layout = [
            [sg.Text('Connection status:' +check_connection())],
            [sg.Text('Please enter your Name, Location and you monthy income')],
            [sg.Text('Name',  font=local_settings.FONT_LARGE), sg.InputText('name')],
            [sg.Text('Location', font=local_settings.FONT_LARGE), sg.InputCombo(('CORK_CITY', 'DUBLIN_CITY', 'GALWAY_CITY', 'LIMERICK_CITY'), font=local_settings.FONT_SMALL)],
            [sg.Text('Price', font=local_settings.FONT_LARGE), sg.InputText(('Enter your monthly salary'), font=local_settings.FONT_SMALL)],
            [sg.Text('Buy or Rent', font=local_settings.FONT_LARGE), sg.InputCombo(('RESIDENTIAL_RENT', 'RESIDENTIAL_SALE'), font=local_settings.FONT_SMALL)],
            [sg.Text('Property Type', font=local_settings.FONT_LARGE), sg.InputCombo(('HOUSE', 'APARTMENT'), font=local_settings.FONT_SMALL)],
          [ sg.Submit(), sg.Cancel()]
         ]
# 

button, values = form.Layout(layout).Read()

if button == "Submit":
    user = Person(values[0], values[1], int(float(values[2])), values[3], values[4])
    print(button, values[0], values[1], values[2], values[3], values[4])
    print(user)

# second window

form = sg.FlexForm('Welcome ' +user.name)  # begin with calculation form

layout = [
          [sg.Text('System is searching for your dream property')], 
          [sg.Text('Your monthly salary is ' +str(user.price))],
          [sg.Text('Your desired location is ' +user.where)],
          [sg.Text('You going for ' +user.action)],
          [sg.Text('Your property type ' +user.kind)],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.Layout(layout).Read()

if button == "Submit":

    daft = Daft()
    if user.where =="DUBLIN_CITY":
        daft.set_location(Location.DUBLIN_CITY)
    elif user.where == "GALWAY_CITY":
        daft.set_location(Location.GALWAY_CITY)
    elif user.where == "LIMERICK_CITY":
        daft.set_lcoation(Location.LIMERICK_CITY)
    else:
        daft.set_location(Location.CORK_CITY)

    if user.kind == "RESIDENTIAL_SALE":
        daft.set_search_type(SearchType.RESIDENTIAL_SALE)
    else:
        daft.set_search_type(SearchType.RESIDENTIAL_RENT)

    daft.set_sort_type(SortType.PRICE_ASC)
    daft.set_max_price(Person.calc_price(user))

listings = daft.search(max_pages=2)
    
layout = []

layout =  [[sg.Text(f'{listing.title}. '), sg.In(key=listing)] for listing in listings]

    #print(listing.title)
layout += [[sg.Button('Save'), sg.Button('Exit')]]
window = sg.Window('To Do List Example', layout)
event, values = window.read()
