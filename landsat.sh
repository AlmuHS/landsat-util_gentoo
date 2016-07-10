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



#This is a script to install landsat-util in gentoo with pip utils, which must be execute as superuser
#It can has many errors, so you can use under your responsability

#Configure portage to add testing libraries support
echo ">=sci-libs/gdal-2.0 ~amd64" >> /etc/portage/package.accept_keywords
echo ">=dev-python/cython-0.23 ~amd64" >> /etc/portage/package.accept_keywords

#Install dependencies
emerge --ask gdal cython sci-libs/atlas dev-python/pip dev-libs/zthread dev-lang/cfortran virtual/lapack

#Download modified ebuild
cd /usr/portage/sci-libs/gdal/
mv gdal-2.0.2.ebuild gdal-2.0.2.ebuild~
wget https://raw.githubusercontent.com/AlmuHS/landsat-util_gentoo/master/gdal-2.0.2.ebuild
repoman manifest

#Reemerge gdal with modified ebuild
emerge gdal

#Install landsat-util
pip install landsat-util


