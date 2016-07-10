#/bin/sh

#This is a script to install landsat-util in gentoo with pip utils, which must be execute as superuser
#It can has many errors, so you can use under your responsability

#Configure files to add testing libraries support
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


