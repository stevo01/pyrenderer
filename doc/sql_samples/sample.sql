SELECT id, lat, lon, geom, tags
	FROM public.planet_osm_nodes
	JOIN public.planet_osm_point 
	ON (planet_osm_nodes.id = planet_osm_point.osm_id);