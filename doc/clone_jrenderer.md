

git clone https://github.com/OpenNauticalChart/renderer.git
cd renderer
cd jsearch
ant
cd ../../


svn co https://josm.openstreetmap.de/osmsvn/applications/editors/josm/plugins/seachart
cd seachart/jrender/
ant
cd ..
	
svn co https://josm.openstreetmap.de/osmsvn/applications/editors/josm/
