import hashlib 
from datetime import datetime

class Block(object):
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8'))
        sha.update(str(self.timestamp).encode('utf-8'))
        sha.update(str(self.data).encode('utf-8'))
        if isinstance(self.previous_hash, (bytes, bytearray)):
            sha.update(self.previous_hash)
        else:
            sha.update(self.previous_hash.encode('utf-8'))
        return sha.hexdigest()

    def __repr__(self):
        return "<Block {} '{}'>".format(self.index, self.hash)

    def toJSON(self):
        return dict(
            index=self.index,
            timestamp=str(self.timestamp),
            data=self.data,
            hash=self.hash
        )


def next_block(data, last_block: Block):
    this_index = last_block.index + 1
    this_timestamp = datetime.utcnow()
    this_data = data
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)