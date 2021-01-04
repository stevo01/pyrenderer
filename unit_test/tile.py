'''
Created on Jan 2, 2021

@author: stevo
'''
import unittest
from utils.map_bb import conversion_type, num2MapBB
from utils.conversions import deg2num


class Test(unittest.TestCase):

    def test_convert_002(self):
        # <node id="583525261" version="6" timestamp="2018-09-20T08:38:47Z" uid="8354582" user="ukraso" changeset="62755031" lat="44.0472726" lon="15.3004193">

        x,y = deg2num(44.0472726, 15.3004193, 9)

        map = num2MapBB(x, y, 9, conversion_type.normal)
        print("bb_norm z=9 {}".format(map.getinfo()))
        print("bb {}".format(map.geojson()))
        print("bb x={},y={},z={}".format(x, y,9))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()