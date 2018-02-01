# This module make a dictionary compose of 3 dictionary for pairs: BTC, ETH, USDT.
# it will store the actual price in BTC(satoshis).
#   e.g. pairDictionary = {"BTC":{"omg":0.0005, "nas":0.0014...}, "ETH":{"omg":0.0006, "nas":0.0017...}...


from HuobiService import *
import pprint

symbols = get_symbols()                      # symbols is a dictionary  containing all the currencies and their pairs.
# pprint.pprint(symbols, width=1)            # to check what is symbols.
# pprint.pprint(symbols['data'][0], width=1) # check a simple trading pair

pairs = {'btc': [], 'eth': [], 'usdt': []}
# dict of 3 arrays. each one will store the currencies that can be trade against their key 'btc','eth' or 'usdt'
# e.g. pair['btc'] = all currencies that can be trade with btc.

main_cryptos ={'btc', 'eth', 'usdt'}
# 3 main cryptos that can be used to trade other altcoins.

# store in pairs the correspondent currencies.
for i in symbols['data']:
    for j in main_cryptos:
        if j in i['quote-currency']:
            pairs[j].append(i['base-currency'])


# Create a list including all currencies with 2 or 3 trading pairs. e.g. omg(btc,eth,usdt), nas(btc,eth)...
def create_trading_list(pairs):
    # Assume all coins are in btc pair.
    # for currency in pairs['btc']:
    tradingList = []  # used to store all currencies (nas,qash...) with 2 or more trading pairs.
    # onlyBTCpair=[]  # used to store all currencies with just one trading pair (btc pair).
    for currency in pairs['btc']:
        if any(currency_eth == currency for currency_eth in pairs['eth']):
            tradingList.append(currency)
        elif any(currency_usdt == currency for currency_usdt in pairs['usdt']):
            tradingList.append(currency)
    #   else:
    #       onlyBTCpair.append(currency)
    # print "Coins with just BTC pair: ",onlyBTCpair
    return tradingList


tradingList = create_trading_list(pairs) # final trading list. list with all currencies with 2 or more trading pairs.
