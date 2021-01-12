# build java applications

## clone and build jsearch
```
git clone https://github.com/OpenNauticalChart/renderer.git
cd renderer
cd jsearch
ant
cd ../../
```

## clone and build jrender
```
svn co https://josm.openstreetmap.de/osmsvn/applications/editors/josm/plugins/seachart
cd seachart/jrender/
ant
cd ..
```

## clone josm (for debugging)
```
svn co https://josm.openstreetmap.de/osmsvn/applications/editors/josm/
```

#Bookmarks:
 https://josm.openstreetmap.de/wiki/DevelopersGuide
