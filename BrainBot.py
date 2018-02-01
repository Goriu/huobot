from HuobiService import *
# import json
# import time

Currencies = ['eos','omg','ruff','zil','soc','mee','eko','link','iost']

DIC = {}
if __name__ == '__main__':

    # Get all the initial info for the crypto pairs in all the markets
    for x in Currencies:
        DIC[x]= []
        # For BTC Market
        y = get_depth(x + 'btc','step0')
        if y['status'] == 'fail':
            DIC[x].append(-1)
            DIC[x].append(-1)
        else:
            DIC[x].append(y['tick']['bids'][0][0])
            DIC[x].append(y['tick']['asks'][0][0])
        # For ETH Market
        y = get_depth(x + 'eth', 'step0')
        if y['status'] == 'fail':
            DIC[x].append(-1)
            DIC[x].append(-1)
        else:
            DIC[x].append(y['tick']['bids'][0][0])
            DIC[x].append(y['tick']['asks'][0][0])
        # For USDT Market
        y = get_depth(x + 'usdt', 'step0')
        if y['status'] == 'fail':
            DIC[x].append(-1)
            DIC[x].append(-1)
        else:
            DIC[x].append(y['tick']['bids'][0][0])
            DIC[x].append(y['tick']['asks'][0][0])


    # Get the values of BTC/USDT and ETH/BTC
    btcusdt = get_depth('btcusdt','step0')['tick']['bids'][0][0]
    ethbtc = get_depth('ethbtc', 'step0')['tick']['bids'][0][0]

    # Normalize all the values of eth and usdt to BTC, so we can compare them
    for x in DIC:
        for i in range(0, len(DIC[x])):
            if i == 2 or i == 3:
                DIC[x][i] = DIC[x][i] * ethbtc
            elif i == 4 or i == 5:
                DIC[x][i] = DIC[x][i] / btcusdt

    print DIC