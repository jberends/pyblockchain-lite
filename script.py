#!/usr/bin/env python
"""
This script is part of package `pyblock_lite`Created by: jochem.berends <jochem.berends@ke-works.com>"""
from pykechain import get_project
import sys

import json

from block.blockchain import get_blockchain
from block.block import next_block

MAXBLOCKS=10000

__version__ = '0.0.1'

def main(**kwargs):
    """
    Main entry point of the script

    :param kwargs:
    :return:
    """
    # # to get the project in KE-chain, uncomment the following line
    # project = get_project()

    # <insert your python magic here>
    blockchain = get_blockchain()
    previous_block = blockchain[-1]

    with open('data/bible.txt','r') as fd:
        for regel in fd:
            block_to_add = next_block(regel, previous_block)
            blockchain.append(block_to_add)

            previous_block = block_to_add
            # sys.stdout.write('.')
            # print("Block #{} with hash '{}' has been added to the blockchain".format(block_to_add.index, block_to_add.hash))

            if block_to_add.index >= MAXBLOCKS:
                break
            

    print('done')

    json.dump([b.toJSON() for b in blockchain], open('data/blockchain.json', 'w'))


if __name__ == '__main__':
    main()