'''
Created on Jan 2, 2021

@author: stevo
'''
import unittest
from utils.map_bb import conversion_type, num2MapBB


class Test(unittest.TestCase):

    def test_convert_ext_z9(self):
        # sample 272-164-9.osm
        # <bounds minlat='53.64463782' minlon='11.07421875' maxlat='54.26522408' maxlon='12.12890625'/>
        tilemap = num2MapBB(272, 164, 9, conversion_type.extendet)
        print("bb_ext  z=9 {}".format(tilemap.getinfo()))
        self.assertAlmostEqual(tilemap.minlat, 53.64463782)
        self.assertAlmostEqual(tilemap.minlon, 11.07421875)
        self.assertAlmostEqual(tilemap.maxlat, 54.26522408)
        self.assertAlmostEqual(tilemap.maxlon, 12.12890625)

    def test_convert_ext_z9_min(self):
        tilemap = num2MapBB(0, 0, 9, conversion_type.extendet)
        print("bb_ext  z=9 {}".format(tilemap.getinfo()))
        self.assertAlmostEqual(tilemap.maxlat, 90)
        self.assertAlmostEqual(tilemap.minlon, -180)

    def test_convert_ext_z9_max(self):
        tilemap = num2MapBB(511, 511, 9, conversion_type.extendet)
        print("bb_ext  z=9 {}".format(tilemap.getinfo()))
        self.assertAlmostEqual(tilemap.minlat, -90)
        self.assertAlmostEqual(tilemap.maxlon, 180)

    def test_convert_ext_z10(self):
        # sample: 544-328-10.osm
        # <bounds minlat='53.85252660' minlon='11.07421875' maxlat='54.26522408' maxlon='11.77734375'/>

        tilemap = num2MapBB(544, 328, 10, conversion_type.extendet)
        print("bb_ext  z=12 {}".format(tilemap.getinfo()))
        self.assertAlmostEqual(tilemap.minlat, 53.85252660)
        self.assertAlmostEqual(tilemap.minlon, 11.07421875)
        self.assertAlmostEqual(tilemap.maxlat, 54.26522408)
        self.assertAlmostEqual(tilemap.maxlon, 11.77734375)

    def test_convert_ext_z11(self):
        # sample: 1089-657-11.osm
        # <bounds minlat='53.85252660' minlon='11.25000000' maxlat='54.16243397' maxlon='11.77734375'/>
        tilemap = num2MapBB(1089, 657, 11, conversion_type.extendet)
        print("bb_ext  z=12 {}".format(tilemap.getinfo()))
        self.assertAlmostEqual(tilemap.minlat, 53.85252660)
        self.assertAlmostEqual(tilemap.minlon, 11.25000000)
        self.assertAlmostEqual(tilemap.maxlat, 54.16243397)
        self.assertAlmostEqual(tilemap.maxlon, 11.77734375)

    def test_convert_ext_z12(self):
        # sample: 2176-1315-12.osm
        # <bounds minlat='53.90433816' minlon='11.16210938' maxlat='54.05938789' maxlon='11.42578125'/>
        tilemap = num2MapBB(2176, 1315, 12, conversion_type.extendet)
        print("bb_ext  z=12 {}".format(tilemap.getinfo()))
        self.assertAlmostEqual(tilemap.minlat, 53.90433816)
        self.assertAlmostEqual(tilemap.minlon, 11.16210938)
        self.assertAlmostEqual(tilemap.maxlat, 54.05938789)
        self.assertAlmostEqual(tilemap.maxlon, 11.42578125)

    def test_convert_002(self):
        map = num2MapBB(272, 164, 9, conversion_type.normal)
        print("bb_norm z=9 {}".format(map.getinfo()))


if __name__ == "__main__":
    unittest.main()
