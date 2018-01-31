from HuobiService import *
# import json
# import time

Currencies = ['eos','omg','ruff','zil','soc','mee','eko','link','iost']

BTCBUY= []
ETHBUY = []
USDTBUY = []
BTCSELL = []
ETHSELL = []
USDTSELL = []
MAX=[]
MIN = []

if __name__ == '__main__':

    #I get all the initial info for the crypto pairs in all the markets
    for x in Currencies:
        #For BTC Market
        y = get_depth(x + 'btc','step0')
        if y['status'] == 'fail':
            BTCBUY.append('-1')
            BTCBUY.append('-1')
        else:
            BTCBUY.append(y['tick']['bids'][0][0])
            BTCSELL.append(y['tick']['asks'][0][0])
        #For ETH Market
        y = get_depth(x + 'eth', 'step0')
        if y['status'] == 'fail':
            ETHBUY.append('-1')
            ETHSELL.append('-1')
        else:
            ETHBUY.append(y['tick']['bids'][0][0])
            ETHSELL.append(y['tick']['asks'][0][0])
        #For USDT Market
        y = get_depth(x + 'usdt', 'step0')
        if y['status'] == 'fail':
            USDTBUY.append('-1')
            USDTSELL.append('-1')
        else:
            USDTBUY.append(y['tick']['bids'][0][0])
            USDTSELL.append(y['tick']['asks'][0][0])



    #Get the values of BTC/USDT and ETH/BTC
    btcusdt = get_depth('btcusdt','step0')['tick']['bids'][0][0]
    ethbtc = get_depth('ethbtc', 'step0')['tick']['bids'][0][0]

    #Normalize all the values of eth and usdt to BTC, so we can compare them
    for i in range(0,len(USDTBUY)):
        USDTBUY[i] = int(USDTBUY[i])/btcusdt
        USDTSELL[i] = int(USDTSELL[i])/btcusdt
    for i in range(0,len(ETHBUY)):
        ETHBUY[i] = ETHBUY[i] * ethbtc
        ETHSELL[i] = ETHSELL[i] * ethbtc

    for i in range(0, len(USDTBUY)):
       MAX.append(max(ETHBUY[i],ETHSELL[i],BTCBUY[i],BTCSELL[i],USDTBUY[i],USDTSELL[i]))
       MIN.append(min(ETHBUY[i], ETHSELL[i], BTCBUY[i], BTCSELL[i], USDTBUY[i], USDTSELL[i]))
    print MAX
    print MIN