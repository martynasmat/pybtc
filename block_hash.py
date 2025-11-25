import struct

from bitcoin.rpc import RawProxy
import hashlib as h
from binascii import unhexlify, hexlify

p = RawProxy()
blockheight = int(input("Enter block height: "))
blockhash = p.getblockhash(blockheight)
block = p.getblock(blockhash)

# Element tx contains the list of all transaction IDs in the block
transactions = block['tx']
block_value = 0

version = hex(int(block['version']))[2:]
prev_block_hash = block['previousblockhash']
merkle_root = block['merkleroot']
time = hex(int(block['time']))[2:]
bits = block['bits']
nonce = hex(int(block['nonce']))[2:]

header_bin = unhexlify(version + prev_block_hash + merkle_root + time + bits + nonce)
hash_out = h.sha256(h.sha256(header_bin).digest()).digest()
print(hexlify(hash_out).decode("utf-8"))
print(hexlify(hash_out[::-1]).decode("utf-8"))
print(hash_out)