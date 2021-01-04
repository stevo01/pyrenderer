'''
Created on Dec 31, 2020

@author: stevo
'''
import sys, os
import shapely.wkb as wkblib
import osmium
import argparse
from shapely.geometry import box
import timeit

area = box(11.074219, 54.265224, 12.128906, 53.644638)

# A global factory that creates WKB from a osmium geometry
wkbfab = osmium.geom.WKBFactory()

class CounterHandler(osmium.SimpleHandler):
    def __init__(self, writer):
        osmium.SimpleHandler.__init__(self)
        self.writer=writer
        self.num_nodes = 0
        self.num_rels = 0
        self.num_ways = 0
        self.nodes = list()
        self.ways = list()
        self.refs = list()
        
        #self.area = box(11.074219, 54.265224, 12.128906, 53.644638)
        
    def node(self, n):
        self.num_nodes += 1
        
        # nodes.append(n)
        
        '''
        if len(n.tags) is 0:
            return
        
        try:
            wkb = wkbfab.create_point(n)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return
        
        point = wkblib.loads(wkb, hex=True)
 
        temp = point.intersection(area)
        if(temp.length != 0.0):
            writer.add_node(n)
        '''
        
    def relation(self, r):
        self.num_rels += 1
        # for entry in r.members:
        #     print(entry)
        print(r.id, r.tags)
            
    
    def way(self, w):
        self.num_ways += 1
 
        #self.ways.append(w.replace(user=""))
         
        try:
            wkb = wkbfab.create_linestring(w)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return
        
        line = wkblib.loads(wkb, hex=True)
 
        temp = line.intersection(area)
        if(temp.length != 0.0):
            writer.add_way(w)

        
if __name__ == '__main__':

    start = timeit.default_timer()
    
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-o', 
                        dest='filename', 
                        type=argparse.FileType('r', encoding='UTF-8'),
                        default="../../volumes/next.osm",
                        help='name of osm file')
    
    args = parser.parse_args()
    filename=args.filename.name
    print(filename)

 
    outfile = filename+'out.osm'
    if os.path.exists(outfile):
        os.remove(outfile)
    writer = osmium.SimpleWriter(outfile)
    
    h = CounterHandler(writer)
    h.apply_file(filename, locations=True, idx='flex_mem')
    
    print("Number of nodes: %d" % h.num_nodes)
    print("Number of ways : %d" % h.num_ways)
    print("Number of rels : %d" % h.num_rels)
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    