# Jamiel Sheikh - jamiel@chainhaus.com
import requests, json

### Run geth --rpc and hit the local HTTP RPC API of a local Eth node

url = 'http://127.0.0.1:8545'
headers = {'Content-type': 'application/json'}
method = 'web3_clientVersion'
data = '{"jsonrpc":"2.0", "method":"{0}", "params":[],"id":100}'
method=data.format('web3_clientVersion')
r = requests.post(url, data = data.format(method), headers= headers)
print(r.text)