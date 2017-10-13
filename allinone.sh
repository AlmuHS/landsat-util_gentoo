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


#This is a script to download and process images using landsat-utils

#The script download the latest landsat'scene_list file, and download and process the images selected from user 
#To do this, the scripts runs a python script, which ask parameters to user and generated a filtered file 
#with the identifiers from images to download

#This script also have many mechanism to protect from errors. 
#If the process is stopped before the end, and is restarted after this, the process will continue from the latest file previous to stop.
#If there are connection problems and any images isn't download correctly, the program repeat the download until this is correct.


FILENAME=filtered_list
DOWNLOAD_PATH="$HOME/landsat/downloads"
PROCESSED_PATH="$HOME/landsat/processed"

#Download latest scene_list
wget http://landsat-pds.s3.amazonaws.com/scene_list.gz
gzip -df scene_list.gz

#Process scene_list to obtain the references
python2 scene_list_filtered.py


#Read images references from filtered_list and execute the commands
while read line
do      

	#Check if that image has not been processed yet	
	if test ! -f "$PROCESSED_PATH/$line/$line"_bands_8432.TIF
	then	
		#Try until the download is successful  			
		while test $(ls $DOWNLOAD_PATH/$line 2>/dev/null | wc -l) -lt 6
		do
			#Download the no-processed image files				
			landsat download $line -b 8432
		done

		#Process the image
		landsat process $DOWNLOAD_PATH/$line -b 8432 --pansharpen

		#Remove no-processed files to save disk space	
		rm -r $DOWNLOAD_PATH/$line
	fi
done < $FILENAME
