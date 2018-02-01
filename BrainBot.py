from HuobiService import *
from PairDictionary import *
# import json
# import time

#  currencies = ['eos','omg','ruff','zil','soc','mee','eko','link','iost','qash']
'''currencies = tradingList  # List from PairDictionary.py. It contains all currencies with 2 or  3 trading pairs.
# currencies = [x.encode('UTF8') for x in currencies] #  convert unicode into utf8 (normal python2.7 string)

print currencies
print "len Currencies: ",len(currencies)'''

currencies = [u'link', u'swftc', u'dash', u'pay', u'evx', u'tnt', u'bch', u'tnb', u'theta', u'dat', u'mana', u'xrp', u'snt', u'utk', u'mco', u'ht', u'rcn', u'qun', u'wax', u'neo', u'salt', u'btm', u'eko', u'srn', u'appc', u'cmt', u'req', u'icx', u'ocn', u'zec', u'act', u'ost', u'storj', u'hsr', u'soc', u'elf', u'ven', u'gnt', u'dbc', u'trx', u'powr', u'zil', u'mee', u'nas', u'ltc', u'eos', u'iost', u'yee', u'ruff', u'rdn', u'lun', u'gnx', u'ela', u'dgd', u'eth', u'smt', u'itc', u'omg', u'stk', u'mds', u'adx', u'etc', u'aidoc', u'qtum', u'cvc', u'qsp', u'bat', u'qash', u'xem', u'gas', u'chat', u'zla', u'topc', u'propy', u'wicc']

DIC = {}
if __name__ == '__main__':

    # Get all the initial info for the crypto pairs in all the markets
    for x in currencies:
        DIC[x]= []
        print DIC[x]
        # For BTC Market
        y = get_depth(x + 'btc','step0')
        if y['status'] == 'fail':
            DIC[x].append(-1)
            DIC[x].append(999999999999)
        else:
            DIC[x].append(y['tick']['bids'][0][0])
            DIC[x].append(y['tick']['asks'][0][0])
        # For ETH Market
        y = get_depth(x + 'eth', 'step0')
        if y['status'] == 'fail':
            DIC[x].append(-1)
            DIC[x].append(999999999999)
        else:
            DIC[x].append(y['tick']['bids'][0][0])
            DIC[x].append(y['tick']['asks'][0][0])
        # For USDT Market
        y = get_depth(x + 'usdt', 'step0')
        print y
        if y['status'] == 'fail':
            DIC[x].append(-1)
            DIC[x].append(999999999999)
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

    #  First is selected the max buy order from the 3 markets (btc/eth/usdt), then from that, selects the lowest sell
    #  from the other 2 markets

    for x in DIC:
        maximum= max(DIC[x][0],DIC[x][2],DIC[x][4])
        if maximum == DIC[x][0]:
            minimum = min(DIC[x][3],DIC[x][5])
            if minimum == DIC[x][3]:
                profit = maximum / minimum
                profit1 = maximum - minimum
                print 'Buy ' + x +' in BTC Market Y sell it in ETH with a % profit of: ', profit, " and a total profit of: ", profit1, " btc"
            elif minimum == DIC[x][5]:
                profit = maximum / minimum
                profit1 = maximum - minimum
                print 'Buy ' + x + ' in BTC Market Y sell it in USDT with a % profit of: ', profit, " and a total profit of: ", profit1, " btc"
        if maximum == DIC[x][2]:
            minimum = min(DIC[x][1],DIC[x][5])
            if minimum == DIC[x][1]:
                profit = maximum / minimum
                profit1 = maximum - minimum
                print 'Buy ' + x + ' in ETH Market Y sell it in BTC with a % profit of: ', profit, " and a total profit of: ", profit1, " btc"
            elif minimum == DIC[x][5]:
                profit = maximum / minimum
                profit1 = maximum - minimum
                print 'Buy ' + x + ' in ETH Market Y sell it in USDT with a % profit of: ', profit, " and a total profit of: ", profit1, " btc"
        if maximum == DIC[x][4]:
            minimum = min(DIC[x][1],DIC[x][3])
            if minimum == DIC[x][1]:
                profit = maximum / minimum
                profit1 = maximum - minimum
                print 'Buy ' + x + ' in USDT Market Y sell it in BTC with a % profit of: ', profit, " and a total profit of: ", profit1, " btc"
            elif minimum == DIC[x][3]:
                profit = maximum / minimum
                profit1 = maximum - minimum
                print 'Buy ' + x + ' in USDT Market Y sell it in ETH with a % profit of: ', profit, " and a total profit of: ", profit1, " btc"





