from HuobiService import *
import json
import time

Currencies = ['eos','omg','ruff','zil','soc','mee','eko','link','iost']
BTC = []
ETH = []
USDT = []

if __name__ == '__main__':

    #I get all the initial info for the crypto pairs in all the markets
    for x in Currencies:
        #For BTC Market
        y = get_depth(x + 'btc','step0')
        if y['status'] == 'fail':
            BTC.append('-1')
        else:
            BTC.append(y['tick']['bids'][0][0])
        #For ETH Market
        y = get_depth(x + 'eth', 'step0')
        if y['status'] == 'fail':
            ETH.append('-1')
        else:
            ETH.append(y['tick']['bids'][0][0])
        #For USDT Market
        y = get_depth(x + 'usdt', 'step0')
        if y['status'] == 'fail':
            USDT.append('-1')
        else:
            USDT.append(y['tick']['bids'][0][0])
    #Get the values of BTC/USDT and ETH/BTC
    btcusdt = get_depth('btcusdt','step0')['tick']['bids'][0][0]
    ethbtc = get_depth('ethbtc', 'step0')['tick']['bids'][0][0]

    #Normalizing all the values of eth and usdt to BTC, so we can compare them
    for i in range(0,len(USDT)):
        USDT[i] = int(USDT[i])/btcusdt
    for i in range(0,len(ETH)):
        ETH[i] = ETH[i] * ethbtc

    print ETH
    print BTC
    print USDT