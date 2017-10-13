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



'''This is a Python script to obtain images references from scene_list file
This script don't do any filter to images' list, only extracts the images' references of fully scene_list 

'''

#open scene_list file
file = open('scene_list', 'r');
ref_file = open("references_list", 'w');

#Skip header
file.next();

#Read file line to line
for line in file:
	#From the line, extract the image reference
	string = line.split(",");
	reference = string[0];

	#write reference to file
	ref_file.write(reference);
	ref_file.write('\n');
	
file.close();
ref_file.close();

