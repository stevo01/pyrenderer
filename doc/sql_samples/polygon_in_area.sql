SELECT 
	osm_id, way, nodes
FROM 
	planet_osm_polygon
JOIN
	planet_osm_ways
ON 
(planet_osm_polygon.osm_id = planet_osm_ways.id)
WHERE 
	ST_Contains(
		ST_Transform(ST_MakeEnvelope(11.074219, 54.265224, 12.128906, 53.644638, 4326), 3857)
		,planet_osm_polygon.way
	);