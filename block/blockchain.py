from .genesis import create_genesis_block

__blockchain = []


def get_blockchain():
    global __blockchain
    if not __blockchain:
        return [create_genesis_block()]
    else:
        return __blockchain