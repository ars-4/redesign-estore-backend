import requests
import os

api_key = os.environ.get('API_KEY')

r = requests.post("https://eth-mainnet.g.alchemy.com/v2/" + api_key, json={"jsonrpc":"2.0","method":"eth_accounts","params":[],"id":1})
r.headers['Content-Type'] = 'application/json'
r.headers['Accept'] = 'application/json'
print(r.text)