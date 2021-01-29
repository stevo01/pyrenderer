#  


# check

## command line option
```
 --debug jdbc:postgresql://192.168.1.54:5432/gis?user=renderer&password=renderer  9 272 164 ./test.png
```

<bounds minlon="10.8013509" maxlon="12.351854965730578" minlat="53.64491939913493" maxlat="54.61558558368226">

INFO: minlat 53.64491939913493, maxlat 54.61558558368226, minlon 10.8013509, maxlon 12.351854965730578

## sql query

SELECT st_transform(way,4326) as mygeom, *
  FROM planet_osm_point
  WHERE tags?'seamark:type' AND way && st_setsrid(st_makebox2d(st_makepoint(1232776.392183322,7103140.164484858), st_makepoint(1350183.6676293542,7220547.439930891)),3857)

SELECT st_transform(way,4326) as mygeom, *
  FROM planet_osm_line
  WHERE tags?'seamark:type' AND way && st_setsrid(st_makebox2d(st_makepoint(1232776.392183322,7103140.164484858), st_makepoint(1350183.6676293542,7220547.439930891)),3857)

SELECT st_transform(way,4326) as mygeom, *
  FROM planet_osm_polygon
  WHERE tags?'seamark:type' AND way && st_setsrid(st_makebox2d(st_makepoint(1232776.392183322,7103140.164484858), st_makepoint(1350183.6676293542,7220547.439930891)),3857)
