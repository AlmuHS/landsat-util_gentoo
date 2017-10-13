#!/usr/bin/python

'''Copyright 2016 Almudena Garcia Jurado-Centurion
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

#This is a Python script to obtain the images dates from scene_list file, filtered by date

#open scene_list file
file = open('scene_list', 'r');
date_file = open("date_list", 'w');

line = file.readline();

numlines = 0;

while line != "":
	#read the line
	if numlines != 0:
		file.readline();
		line = file.readline();
	else:
		line = file.readline();

	if line != "":	
		#Extract the image date and reference
		string = line.split(",");
		reference = string[0];
		date = string[1];
	
		#Extract the images' year
		day = date.split(" ");
		filter_day = day[0].split("-");
		year = filter_day[0]
	
		numlines += 1;
	

		date_file.write(day[0]);
		date_file.write('\n');

file.close();
date_file.close();

