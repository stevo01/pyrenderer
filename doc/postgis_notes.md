# import data to db

```
export PGPASSWORD=renderer
PG_USER=renderer
PG_DBNAME=gis
PG_HOST=localhost

osm2pgsql -U $PG_USER -H $PG_HOST -d $PG_DBNAME --create -G -s --number-processes 4 -C16000 --hstore osm/xapi-planet.osm
```

# connect psql client with database
```
psql -d $PG_DBNAME --dbname $PG_DBNAME --host $PG_HOST --username $PG_USER
```

# sampe sql queries (from mapnik)
https://trac.openstreetmap.org/browser/applications/rendering/mapnik/osm.xml

# count number of elements
select count(id) from planet_osm_nodes;
select count(id) from planet_osm_rels;
select count(id) from planet_osm_ways;

select count(osm_id) from planet_osm_line;
select count(osm_id) from planet_osm_point;
select count(osm_id) from planet_osm_polygon;
select count(osm_id) from planet_osm_roads;

# database schema

followimg tables are just required for updates of database with osm2psql
  planet_osm_nodes
  planet_osm_rels
  planet_osm_ways

tabled relevant for renderer
  planet_osm_line: contains all imported ways
  planet_osm_point: contains all imported nodes with tags
  planet_osm_polygon: contains all imported polygons. Relations seem to be resolved for that.

not required tables:
  planet_osm_roads



# select points in bounding box
```

SELECT osm_id
FROM planet_osm_point
WHERE ST_Contains(
    ST_Transform(
        ST_MakeEnvelope(11.074219, 54.265224, 12.128906, 53.644638,
        4326)
        ,3857)
    ,planet_osm_point.way);

```

# bookmarks
https://postgis.net/workshops/postgis-intro/geometries_exercises.html
https://www.youtube.com/watch?v=QJF4jLRBFrU
https://2019.stateofthemap.org/attachments/K8N3XY_2019-09-22-talk-sotm2019-osm-postgresql-postgis-en-slides.pdf
