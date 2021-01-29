#!/usr/bin/python3
# encoding: utf-8
from utils.conversions import num2deg


class conversion_type():
    normal = 0
    extendet = 1


# Tile numbers to lon./lat.
def num2MapBB(xtile, ytile, z, conv_type=conversion_type.normal):

    if z < 9 or z > 18:
        return None

    if conv_type == conversion_type.normal:
        min_lat, min_lon = num2deg(xtile, ytile, z)
        max_lat, max_lon = num2deg(xtile + 1, ytile - 1, z)

    elif conv_type == conversion_type.extendet:

        if z == 12:
            offset = 1
        else:
            offset = 2

        z_diff = 12 - z
        factor = pow(2, z_diff)
        x_z12_min = max(xtile * factor - offset, 0)
        y_z12_max = max(ytile * factor - offset, 0)
        x_z12_max = min(xtile * factor + factor + offset, 4096)
        y_z12_min = min(ytile * factor + factor + offset, 4096)

        max_lat, max_lon = num2deg(x_z12_max, y_z12_max, 12)
        min_lat, min_lon = num2deg(x_z12_min, y_z12_min, 12)
    else:
        return None

    ret = MapBB(min_lat, min_lon, max_lat, max_lon)

    return ret


class MapBB:

    def __init__(self, minlat, minlon, maxlat, maxlon):
        self.minlat = minlat
        self.minlon = minlon
        self.maxlat = maxlat
        self.maxlon = maxlon
        self.lat=(minlat + maxlat) / 2
        self.lon=(minlon + maxlon) / 2

    def getbbox(self):
        ret = [self.minlon, self.minlat, self.maxlon, self.maxlat]
        return ret

    def getstring(self):
        ret = ("{:.8f}, {:.8f}, {:.8f}, {:.8f}".format(self.minlat, self.minlon, self.maxlat, self.maxlon))
        return ret

    def getinfo(self):
        ret = ("(minlat {:.8f}, maxlat {:.8f}, minlon {:.8f}, maxlon {:.8f})".format(
                self.minlat,
                self.maxlat,
                self.minlon,
                self.maxlon))

        return ret

    def geojson(self):
        ret = "{ \"type\": \"Feature\", \"geometry\": { \"type\": \"Polygon\", \"coordinates\": [["
        ret += "[{:.8f}, {:.8f}],".format(self.minlon, self.minlat)
        ret += "[{:.8f}, {:.8f}],".format(self.maxlon, self.minlat)
        ret += "[{:.8f}, {:.8f}],".format(self.maxlon, self.maxlat)
        ret += "[{:.8f}, {:.8f}],".format(self.minlon, self.maxlat)
        ret += "[{:.8f}, {:.8f}] ".format(self.minlon, self.minlat)
        ret += "]]}, \"properties\": { }}"

        return ret
    
    def GetOverpassQuery(self):
            out ="[timeout:25];(" 
            out+="way [\"seamark:type\"] ({},{},{},{});".format(self.minlat,self.minlon,self.maxlat,self.maxlon)
            out+="relation [\"seamark:type\"] ({},{},{},{});".format(self.minlat,self.minlon,self.maxlat,self.maxlon)
            out+="node [\"seamark:type\"] ({},{},{},{});".format(self.minlat,self.minlon,self.maxlat,self.maxlon)
            out+=");out meta;"
            
            return out
