select osm_id, tags
  from planet_osm_point
  where tags -> 'seamark:type' = 'bridge'
    limit 20
