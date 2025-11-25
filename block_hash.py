from bitcoin.rpc import RawProxy
import hashlib as h
from binascii import unhexlify, hexlify

p = RawProxy()
blockheight = 277316
blockhash = p.getblockhash(blockheight)
block = p.getblock(blockhash)

# Element tx contains the list of all transaction IDs in the block
transactions = block['tx']
block_value = 0

version = block['version']
prev_block_hash = block['previousblockhash']
merkle_root = block['merkleroot']
nonce = block['nonce']
time = block['time']
bits = block['difficulty']

header_bin = unhexlify(hex(version) + prev_block_hash + merkle_root + hex(nonce) + hex(time) + hex(bits))
hash_val = h.sha256(h.sha256(header_bin).digest()).digest()
print(hexlify(hash_val).decode('utf-8'))
