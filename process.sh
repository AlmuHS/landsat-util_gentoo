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



#This script process the images downloaded from download.sh, using landsat-utils
#This script DON'T DOWNLOAD, ONLY PROCESS

FILENAME=filtered_list

LANDSAT_PATH=$HOME/landsat/downloads

while read line     
do        
	landsat process $LANDSAT_PATH/$line -b 432 --pansharpen
	rm -r $LANDSAT_PATH/$line
done < $FILENAME
