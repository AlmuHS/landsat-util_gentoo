#!/bin/sh

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



#This is a script to install landsat-util in Debian with pip utils, which must be execute as superuser
#It can has many errors, so you can use under your responsability

apt-get update
apt-get install python-pip python-numpy python-scipy libgdal-dev libatlas-base-dev gfortran libfreetype6-dev libgnutls28-dev
pip install landsat-util
