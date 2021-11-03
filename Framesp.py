from web3 import Web3
from web3.middleware import geth_poa_middleware

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))

latest_Block = web3.eth.getBlock('latest')
print("Latest Block of ethereum blockchain:",latest_Block)

ton = web3.eth.get_block_transaction_count(13537137) 
print("Transaction Count:",ton)

Transactionfee = web3.eth.feehistory(765,'latest',None)
print("Transaction fee:",Transactionfee)