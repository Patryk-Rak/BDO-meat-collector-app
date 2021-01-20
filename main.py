from tinydb import TinyDB, Query
from tkinter import *
from tkinter.ttk import *
import datetime
import platform
from datetime import date

try:
        import winsound #windows
except:
        import os #other

gathering_data = TinyDB('gathering_data.json')
prices = TinyDB('prices.json')
Data = Query()


def insert():
    meat_c = int(input("Put Lamb Meat count: "))
    caphras_c = int(input("Put Caphras count: "))
    gem_fragment_c = int(input("Put Gem Fragment count: "))
    sharp_shard_c = int(input("Put Sharp Shards count: "))
    hard_shard_c = int(input("Put Hard Shards count: "))
    time_c = int(input("Put time in minutes how long you gathered: "))
    gathering_data.insert({'meat': meat_c, 'caphras': caphras_c, 'gem_fragment': gem_fragment_c, 'sharp_shard': sharp_shard_c, 'hard_shard': hard_shard_c, 'gath_time': time_c})


def show():
#    print(db.all())
    meats = [r['meat'] for r in gathering_data]
    print(meats)


def update_prices(meat_price, caphra_price, gem_price, sharp_price, hard_price):
    prices.update({'meat_price': meat_price, 'caphras_price': caphra_price, 'gem_fragment_price': gem_price,
               'sharp_shard_price': sharp_price, 'hard_shard_price': hard_price}, doc_ids=[1])


def check_actual_prices():
    get_meat_price = [r['meat_price'] for r in prices]
    get_caphras_price = [r['caphras_price'] for r in prices]
    get_gem_fragment_price = [r['gem_fragment_price'] for r in prices]
    get_sharp_shard_price = [r['sharp_shard_price'] for r in prices]
    get_hard_shard_price = [r['hard_shard_price'] for r in prices]
    return(f"Lamb Meat Price: {'{:,}'.format(get_meat_price[0])} silver\n"
           f"Caphras Price: {'{:,}'.format(get_caphras_price[0])} silver\n"
           f"Gem Fragment Price: {'{:,}'.format(get_gem_fragment_price[0])} silver\n"
           f"Sharp Shard Price: {'{:,}'.format(get_sharp_shard_price[0])} silver\n"
           f"Hard Shard Price: {'{:,}'.format(get_hard_shard_price[0])} silver\n")

def insert_actual_prices():
    insert_meat_price = [r['meat_price'] for r in prices]
    insert_caphras_price = [r['caphras_price'] for r in prices]
    insert_gem_fragment_price = [r['gem_fragment_price'] for r in prices]
    insert_sharp_shard_price = [r['sharp_shard_price'] for r in prices]
    insert_hard_shard_price = [r['hard_shard_price'] for r in prices]
    return(insert_meat_price,insert_caphras_price,insert_gem_fragment_price,insert_sharp_shard_price,insert_hard_shard_price)

# def escape():
#     exit()
#
#
#
# while escape != 1:
# choice = int(input("What you want to do?\n"
# "1 - Add new gathering record\n"
# "2 - Show me gathering list\n"
# "3 - Update prices\n"
# "4 - Quit\n"))
# operations = [insert, show, update_prices, escape]
# output = operations[choice - 1]()
# print(output)
