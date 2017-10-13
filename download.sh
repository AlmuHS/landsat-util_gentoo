#!/bin/bash

#Copyright 2016 Almudena Garcia Jurado-Centurion

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.



#This script download the latest scene_list, launch a python script to generate the identifiers filtered list
#and download the images using landsat-utils
#This script DON'T PROCESS IMAGES, ONLY DOWNLOAD THEM

 
FILENAME=filtered_list

wget http://landsat-pds.s3.amazonaws.com/scene_list.gz
gzip -df scene_list.gz

python scene_list_filtered.py

numline=0;
limit=5;

while read line     
do        
	if test $numline -ne $limit;
	then	
		landsat download $line -b 432
		numline=$(($numline + 1));
	fi
done < $FILENAME
