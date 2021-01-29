'''
Created on Dec 31, 2020

@author: stevo
'''

import argparse
import osmium
from utils.map_bb import conversion_type, num2MapBB


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-x',
                        dest='x',
                        default="272",
                        help='tile x')
    
    parser.add_argument('-y',
                        dest='y',
                        default="164",
                        help='tile y')

    parser.add_argument('-z',
                        dest='z',
                        default="9",
                        help='tile z')
    
    args = parser.parse_args()
    
    
    x=int(args.x)
    y=int(args.y)
    z=int(args.z)
    
    
    
    bb = num2MapBB(x, y, z, conversion_type.extendet)
    
    link = "http://map.openseamap.org/"
    link +="?zoom={}".format(z)
    link += "&lat={}&lon={}".format(bb.lat, bb.lon)
    link += "&mlat={}&mlon={}".format(bb.lat, bb.lon)
    link += "&mtext=x{}_y{}_z{}".format(x,y,z)
    link += "&layers=BFTFFFFFFTF0FFFFFFFFFF"
    print(link)
    
    print("\n\nquery for https://overpass-turbo.eu/")
    print(bb.GetOverpassQuery())
    
    print("\n\ngeojson info:")
    print(bb.geojson()())
    



    

