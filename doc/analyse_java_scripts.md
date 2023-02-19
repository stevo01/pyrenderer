27.12.2020

notes for analysis of java scripts jrenderer and jsearch

# test area
  tile x = 272
  tile y = 164
  tile z = 9

  bb     info(minlat, minlon, maxlat, maxlon) 54.162434, 11.250000, 54.162434, 11.250000
  bb_ext info(minlat, minlon, maxlat, maxlon) 53.644638, 11.074219, 54.265224, 12.128906

  geo json
  { "type": "Feature",
    "geometry": { "type": "Polygon",
                  "coordinates": [[[11.074219, 53.644638],
                                   [12.128906, 53.644638],
                                   [12.128906, 54.265224],
                                   [11.074219, 54.265224],
                                   [11.074219, 53.644638]]]},
    "properties": { }
  }

## load data from overpass api
```
wget -O osm/xapi-272_164_9.osm --timeout=600 --post-file=./query/overpass-api-272_164_9.overpassql "http://overpass-api.de/api/interpreter"
```

## copy extract
```
cp osm/xapi-272_164_9.osm next.osm
```

# create old version of file (allow first call of renderer)
```
touch world.osm
```

# create a diff file
```
diff world.osm next.osm | grep id= | grep -v "<tag" > diffs
```

# check java version
stevo@stone:/media/data/docker/osm-SeaMarkRenderer$ java -version
  openjdk version "1.8.0_222"
  OpenJDK Runtime Environment (build 1.8.0_222-8u222-b10-1~deb9u1-b10)
  OpenJDK 64-Bit Server VM (build 25.222-b10, mixed mode)

# generate osm extracts with jsearch application
```
java -jar ./extutils/jsearch.jar ./tmp 272 164
```


# generate tiles with jrenderer.jar application
```
java -jar ./extutils/jrender.jar workingdir/osm-extracts/ workingdir/tilecache/ 9 272 164
```
