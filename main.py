""" Affordable Price Finder v0.1
    simple app that enables user
    searching for his/her dream house
    for renting in Ireland
    using www.daft.ie """

import pysimplegui as sg

class Person():
    def __init__(self, name, where, price):
        self.name = name
        self.where = where
        self.price = price
    
    def welcome(self):
        print('Hello ' +self.name +' ! Welcome to Dream House Finder')
    
    def show_price(self):
        return self.price

    def change_price(self, value):
        value = self.price
        
