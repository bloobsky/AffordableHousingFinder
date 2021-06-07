""" Affordable Price Finder v0.1
    simple app that enables user
    searching for his/her dream house
    for renting in Ireland
    using www.daft.ie """

import PySimpleGUI as sg
import urllib.request
import local_settings 

def check_connection():
    status_code = urllib.request.urlopen(local_settings.DAFT_URL).getcode()
    if status_code == 200:
        on_or_404 = 'OK'
    else:
        on_or_404 = 'NOT OK'
    
    return on_or_404


conn = check_connection()

class Person():
    def __init__(self, name, where, price):
        self.name = name
        self.where = where
        self.price = price

    def __str__(self):
        return self.name +', ' +self.where +', ' +self.price
    
    def change_price(self, value):
        value = self.price

""" Main Program Loop""" 

# Very basic form.  Return values as a list
form = sg.FlexForm('Dream House Finder')  # begin with a blank form

layout = [
            [sg.Text('Connection status:' +check_connection())],
            [sg.Text('Please enter your Name, Location and you monthy income')],
            [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
            [sg.Text('Location', size=(15, 1)), sg.InputCombo(('Cork', 'Dublin', 'Galway', 'Limerick'), size=(15, 1))],
            [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
          [ sg.Submit(), sg.Cancel()]
         ]

button, values = form.Layout(layout).Read()

user = Person(values[0], values[1], values[2])
print(button, values[0], values[1], values[2])

print(user)

# second window

form = sg.FlexForm('Welcome ' +user.name)  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name, Location and you monthy income')],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.Layout(layout).Read()
