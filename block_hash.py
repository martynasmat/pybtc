from bitcoin.rpc import RawProxy

p = RawProxy()
blockheight = 277316
blockhash = p.getblockhash(blockheight)
block = p.getblock(blockhash)

# Element tx contains the list of all transaction IDs in the block
transactions = block['tx']
block_value = 0

for txid in transactions:
    tx_value = 0
    raw_tx = p.getrawtransaction(txid)
    decoded_tx = p.decoderawtransaction(raw_tx)

    # Iterate through each output in the transaction
    for output in decoded_tx['vout']:

        # Add up the value of each output
        tx_value = tx_value + output['value']

        # Add the value of this transaction to the total
        block_value = block_value + tx_value
print("Total output value (in BTC) in block #277316: ", block_value)