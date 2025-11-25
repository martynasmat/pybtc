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

version = int(block['version'])
prev_block_hash = block['previousblockhash']
merkle_root = block['merkleroot']
time = int(block['time'])
bits = block['bits']
nonce = int(block['nonce'])

print(
f"""
version                     {version}
prev_block_hash             {prev_block_hash}
merkle_root                 {merkle_root}
time                        {time}
bits                        {bits}
nonce                       {nonce}
"""
)

header = (
        version.to_bytes(4, 'little')
        + bytes.fromhex(prev_block_hash)[::-1]
        + bytes.fromhex(merkle_root)[::-1]
        + time.to_bytes(4, 'little')
        + bytes.fromhex(bits)[::-1]
        + nonce.to_bytes(4, 'little')
    )
hash_out = h.sha256(h.sha256(header).digest()).digest()
print(f"Calculated block hash    {hash_out[::-1].hex()}")
print(f"RPC API block hash       {hash_out[::-1].hex()}")
