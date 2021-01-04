SELECT AddGeometryColumn ('planet_osm_nodes','geom',4326,'POINT',2);
UPDATE planet_osm_nodes SET geom = ST_SetSRID(ST_MakePoint( lon , lat ), 4326);