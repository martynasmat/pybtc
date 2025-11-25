import struct

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
time = block['time']
bits = block['bits']
nonce = block['nonce']

print(version)
print(prev_block_hash)
print(merkle_root)
print(hex(time)[2:])
print(bits)
print(hex(nonce)[2:])


header = (
    struct.pack("<L", version) +
    bytes.fromhex(prev_block_hash)[::-1] +
    bytes.fromhex(merkle_root)[::-1] +
    struct.pack("<L", time) +
    bytes.fromhex(bits)[::-1] +
    struct.pack("<L", nonce)
)

block_hash = h.sha256(h.sha256(header).digest()).digest()[::-1].hex()
print(block_hash)