import requests
import json
bob = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=axie-infinity%2Csmooth-love-potion%2Cvigorus%2Crevolution-populi%2Cethereum%2Cbitcoin&vs_currencies=usd", headers = {"accept": "application/json"})
print("AXS Price : " + str(bob.json()['axie-infinity']['usd']))
print("SLP Price : " + str(bob.json()['smooth-love-potion']['usd']))
print("VIS Price : " + str(bob.json()['vigorus']['usd']))
print("RVP Price : " + str(bob.json()['revolution-populi']['usd']))
print("ETH Price : " + str(bob.json()['ethereum']['usd']))
print("BTC Price : " + str(bob.json()['bitcoin']['usd']))
