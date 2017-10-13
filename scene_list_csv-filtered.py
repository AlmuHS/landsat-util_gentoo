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

#This is a simplified version from scene_list_filtered, rewrited using csv python package
#This version don't ask any data to user. Instead, it filtered the images using the filters written in the latest code section


import csv

#Open the destination file
filtered_file = open("filtered_list", 'w');

#Open the original file as csv file
with open('scene_list', 'rb') as csvfile:

	#Obtain the rows from csv file
	scenereader = csv.reader(csvfile, delimiter=',', quotechar=' ')

	#skip the header
	scenereader.next()

	#Read the rows and obtain the arguments
	for row in scenereader:
		reference = row[0]
		date = row[1]	
		cloud_index = row[2]

		#Obtain year and month
		year = date[0:4]
		month = date[5:7]

		#Apply filter and write references in the file
		if year == '2016' and int(month) in range(5,8) and float(cloud_index) < 10:
			filtered_file.write(reference + '\n')

#Close file
filtered_file.close()
			
			
	
