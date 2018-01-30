# This module make a dictionary compose of 3 dictionary for pairs: BTC, ETH, USDT.
# it will store the actual price in BTC(satoshis).
#   e.g. pairDictionary = {"BTC":{"omg":0.0005, "nas":0.0014...}, "ETH":{"omg":0.0006, "nas":0.0017...}...


from HuobiService import *
import pprint

symbols = get_symbols()  # symbols is a dictionary  containing all the currencies and their pairs.
# pprint.pprint(symbols, width=1)  # to check what is symbols.
# pprint.pprint(symbols['data'][0], width=1) # check a simple trading pair

# print 'quote-currency' in symbols['data'][0]  #check if there is a key called 'quote-currency' in symbols
#                                                only for keys(dictionary indexes), not working for values.


# TESTING
key, value = 'quote-currency', 'usdt'
print key in symbols['data'][0] and value == symbols['data'][0][key]  # check if there is a trading pair with USDT.
print 'usdt' in symbols['data'][0].values()  # other way to check if there is a trading pair with USDT
# END OF TESTING

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

# TODO-me create a set (inmutable) with all currencies with 2 or 3 trading pairs. e.g. omgbtc, omgeth...


print pairs

print len(pairs['btc'])  # number of cryptocurrencies for trading in btc pair
print len(pairs['eth'])  # number of cryptocurrencies for trading in eth pair
print len(pairs['usdt'])  # number of cryptocurrencies for trading in usdt pair
print pairs['usdt']
#and value == symbols["data"][0]
#if item in list: ....