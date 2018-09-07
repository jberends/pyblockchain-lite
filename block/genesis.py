# genisis block creation

from datetime import datetime
from .block import Block
import hashlib

def create_genesis_block():
    # manually create the first genesis block with
    # index 0 and som though of hash
    return Block(0, datetime.utcnow(), "Genesis Block", str(datetime.utcnow()).encode('utf-8'))