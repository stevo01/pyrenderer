#!/bin/bash

START=$1
END=$2

for i in $(seq $START $END); 
	do python3 pyextract.py -g -i ./sampledata/in/seamarks_planet.osm -o ./workingdir/ -y $i
done

