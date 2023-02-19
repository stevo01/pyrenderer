# measure extract of single z9 area with osmium
time osmium extract --bbox 11.074219,53.644638,12.128906,54.265224 -o test_osmium.osm next.osm
real	0m15.334s
user	0m15.507s
sys	0m0.529s

# measure extract of single z9 area with jsearch / extract
around 27 sec.

java -jar jsearch.jar ./tmp 272 164

# measure extract of single z9 area with overpass
time wget -O test_overpass.osm --timeout=600 --post-file=./query/overpass-api-272_164_9.overpassql "http://overpass-api.de/api/interpreter"
--2020-12-29 21:04:36--  http://overpass-api.de/api/interpreter
Resolving overpass-api.de (overpass-api.de)... 2a01:4f8:110:502c::2, 2a01:4f8:120:6464::2, 178.63.48.217, ...
Connecting to overpass-api.de (overpass-api.de)|2a01:4f8:110:502c::2|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [application/osm3s+xml]
Saving to: ‘test_overpass.osm’

test_overpass.osm                              [  <=>                                                                                 ] 440.13K  1.17MB/s    in 0.4s

2020-12-29 21:04:41 (1.17 MB/s) - ‘test_overpass.osm’ saved [450693]

real	0m4.589s
user	0m0.017s
sys	0m0.000s


# measure query of single z9 area with psql
select osm_id, tags, ST_AsText(way), way
  from planet_osm_point
  where (tags ? 'seamark:type')
    AND ST_Intersects(
		  ST_Transform(ST_MakeEnvelope(11.074219, 54.265224, 12.128906, 53.644638, 4326), 3857)
		  ,planet_osm_point.way
		);
		
select osm_id, tags, ST_AsText(way), way
  from planet_osm_polygon
  where (tags ? 'seamark:type')
    AND ST_Intersects(
		  ST_Transform(ST_MakeEnvelope(11.074219, 54.265224, 12.128906, 53.644638, 4326), 3857)
		  ,planet_osm_polygon.way
		);	
		
select osm_id, tags, ST_AsText(way), way
  from planet_osm_line
  where (tags ? 'seamark:type')
    AND ST_Intersects(
		  ST_Transform(ST_MakeEnvelope(11.074219, 54.265224, 12.128906, 53.644638, 4326), 3857)
		  ,planet_osm_line.way
		);
		
		

		