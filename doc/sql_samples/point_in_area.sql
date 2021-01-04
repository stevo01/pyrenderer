SELECT 
	osm_id, way, tags
FROM 
	planet_osm_point
WHERE 
	ST_Contains(
		ST_Transform(ST_MakeEnvelope(11.074219, 54.265224, 12.128906, 53.644638, 4326), 3857)
		,planet_osm_point.way
	);