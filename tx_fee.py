from bitcoin.rpc import RawProxy

p = RawProxy()

txid = input("Enter transaction hash: ")

tx = p.getrawtransaction(txid)
tx = p.decoderawtransaction(tx)

vout_sum = sum([i["value"] for i in tx["vout"]])

vin_sum = 0
for vin in tx["vin"]:
    prev = p.getrawtransaction(vin["txid"])
    prev = p.decoderawtransaction(prev)
    prev_vout = prev["vout"][vin["vout"]]
    vin_sum += prev_vout["value"]

fee = vin_sum - vout_sum

print(f"in: {vin_sum}")
print(f"out: {vout_sum}")
print(f"fee: {fee} BTC / {fee * 100000000} SATS")
