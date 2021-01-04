'''
Created on Dec 31, 2020

@author: stevo
'''

import argparse
import osmium


class CounterHandler(osmium.SimpleHandler):

    def __init__(self):
        osmium.SimpleHandler.__init__(self)
        self.num_nodes = 0
        self.num_rels = 0
        self.num_ways = 0

    def node(self, n):
        self.num_nodes += 1

    def relation(self, n):
        self.num_rels += 1

    def way(self, n):
        self.num_ways += 1


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-o',
                        dest='filename',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        default="../../volumes/next.osm1",
                        help='name of osm file')

    args = parser.parse_args()
    filename = args.filename.name
    print(filename)

    h = CounterHandler()

    # h.apply_file(filename, locations=True, idx='dense_file_array,./example.nodecache')
    h.apply_file(filename, locations=True)
    print("Number of nodes: %d" % h.num_nodes)
    print("Number of ways : %d" % h.num_ways)
    print("Number of rels : %d" % h.num_rels)
