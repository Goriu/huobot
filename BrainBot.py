from HuobiService import *
import json
import time

Currencies = ['eos','omg','ruff','zil','soc','mee','eko','link','iost']


if __name__ == '__main__':
    for x in Currencies:
        print "Esto es " + x + " btc"
        y = get_depth(x + 'btc','step0')
        print y['tick']['bids'][0]
        print "Esto es " + x + " eth"
        y = get_depth(x + 'eth', 'step0')
        print y['tick']['bids'][0]
