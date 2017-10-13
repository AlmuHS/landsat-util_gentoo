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


'''
This is a Python script to obtain the images references from scene_list file, filtered by date and cloud index

The script ask to user the parameters to filter the images from scene_list.
This parameters are:

year_max, year_min = year interval in which images were taken.
mount_max, month_min = month interval in which images were taken.
cloud_max = maximal cloud cover
lat_min, lat_max = latitudes range
lon_max, lon_min = longitudes range

With this data, the script filter the images that meet the parameters, and copy their identifiers to a new file
'''


print "Welcome to filtered_list generator"
print "-------------------------------------\n"

#default values
year_min = 2016
year_max = 2016
month_min = 5
month_max = 8
cloud_max = 2.0
lat_min = 12.0
lat_max = 37.0
lon_min = 112.0
lon_max = 154.0

option = 'y'

#Ask parameters
while option == 'y':
	print "\nThe current parameters are:"
	print "year: " + str(year_min) + " - " + str(year_max)
	print "month: " + str(month_min) + " - " + str(month_max) 
	print "cloud_max: " + str(cloud_max)
	print "lat: " + str(lat_min) + " - " + str(lat_max)
	print "lon: " + str(lon_min) + " - " + str(lon_max)

	option = raw_input("Do you want to introduce new parameters? (y/n): ")

	if option == 'y':
		year_min = input("start year: ")
		while year_min < 2013:
			year_min = input("start year: ")

		year_max = input("end year ")
		while year_max < 2013 and year_max < year_min:
			year_max = input("end year ")

		month_min = input("start month: ")
		while month_min > 12 or month_min < 1:
			month_min = input("start month: ")

		month_max = input("end month : ")
		while month_max < month_min or month_max > 12 or month_max < 1:
			month_max = input("end month : ")

		cloud_max = input("max cloud index: ")
		while cloud_max > 100 or cloud_max < 0:
			cloud_max = input("max cloud index: ")

		lat_min = input("minimum latitude: ")
		while lat_min > 90:
			lat_min = input("minimum latitude: ")

		lat_max = input("maximum latitude: ")
		while lat_max < lat_min or lat_max > 90:
			lat_max = input("maximum latitude: ")

		lon_min = input("minimum longitude: ")
		while lon_min > 180:
			lon_min = input("minimum longitude: ")

		lon_max = input("maximum longitude: ")
		while lon_max < lon_min or lon_max > 180:
			lon_max = input("maximum longitude: ")	 

counter = 0

#open scene_list file
file = open('scene_list', 'r');
filtered_file = open("filtered_list", 'w');
		
#Skip header
file.next();

#Read file line to line
for line in file:
	#From line, extract the image date and reference
	string = line.split(",");
	reference = string[0];
	date = string[1];
	cloud = string[2];	
		
	#Obtain year and month
	year = date[0:4]
	month = date[5:7]
	min_lat = string[6]
	min_lon = string[7]
	max_lat = string[8]
	max_lon = string[9]

	

	#Apply filter and write references in the file
	if int(year) in range(year_min, year_max + 1) and int(month) in range(month_min, month_max + 1) and float(cloud) < cloud_max:
		if float(min_lat) > lat_min and float(max_lat) < lat_max and float(min_lon) > lon_min and float(max_lon) < lon_max:
		#if float(min_lat) > 36 and float(max_lat) < 42  and float(min_lon) > 26 and float(max_lon) < 45: #Turquia
			filtered_file.write(reference + '\n')
			counter = counter + 1

print str(counter) + " images found"
file.close();
filtered_file.close();

