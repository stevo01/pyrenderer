# overview
pyrenderer is a collection of scripts to run jrenderer application

# external dependencies

## overpass api
this is needed to fetch osm file with all seamarks from openstreetmap database

## osmium
osmium allows to compare osm files and extract osm files from another osm file

## jrenderer
java application renders sea marks by a given osm file
note: jrenderer is part of josm plugin JOSM-seachart

# setup workbench
## clone the project
```
git clone https://github.com/stevo01/pyrenderer.git
cd pyrenderer
```

## install required applications and libs
```
sudo apt install osmium-tool python3 python3-pip
sudo apt install openjdk-8-jre-headless
pip3 install osmium

sudo apt install libpostgis-java libpostgresql-jdbc-java
libpostgresql-jdbc-java (42.2.5-2).
libpostgis-java (1:2.3.0-1)
```

### java version

the renderer is compatibel and running with Java(TM) SE Runtime Environment (build 1.8.0_xxx)

the following url include install instrations for linux:
https://docs.datastax.com/en/jdk-install/doc/jdk-install/installOracleJdkDeb.html

alternative solution is the openjdk in version 11
```
sudo apt install openjdk-11-jre-headless
```

# example

































usage

the following command sequences generates the sea mark tiles in zoom level 9.18 for following area:

geo json:
	{ "type": "Feature", "geometry": { "type": "Polygon", "coordinates": [[[11.074219, 53.644638],[12.128906, 53.644638],[12.128906, 54.265224],[11.074219, 54.265224],[11.074219, 53.644638] ]]}, "properties": { }}

tile info:
	x = 272, y = 164, z = 9

## files and directories

 name: ./workingdir/in/osm      
 description: osm file(s) from overpass api

 name: ./workingdir/osm-extracts/
 description: osm files generated by pyextract.py / osmium

 name: ./workingdir/tilecache/
 description: tiles generated by pyrender / jrenderer

### tile storage schema

 schema:
    tiles/z/x/y.png

 sample:
    ./9/272/164.png

### filenames osm extracts

 schema:
   x-y-z.osm

 sample:
    272-164-9.osm

## fetch osm file with all seamarks from openstreetmap database (http://overpass-api.de/api/interpreter)
```
mkdir -p workingdir/in/osm
wget -O workingdir/in/osm/seamarks_planet.osm --timeout=600 --post-file=./sampledata/query/overpass-api-planet.ql "http://overpass-api.de/api/interpreter"
```

## generate osm file extract
The following sample generates osm extracts for following tile:
```
python3 pyextract.py -g -i ./workingdir/in/osm/seamarks_planet.osm -o ./workingdir/ -y 164 -x 272
```

## generate tiles
The following sample generates sea mark tiles.

options:
 -o path for storage of generated tiles
 -i path to osm extracts needs to be rendered
 -d run in "server mode" (like a daemon)

```
python3 pyrenderer.py -i ./workingdir/osm-extracts/ -o ./workingdir/tilecache/
```

# bookmarks
  git@github.com:stevo01/renderer.git
  https://github.com/OpenNauticalChart/renderer.git
