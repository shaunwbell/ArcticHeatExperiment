#!/usr/bin/env

"""
worldview_modis_wget.py

Purpose:
	Connect to ketch.pmel.noaa.gov (engineering run system) to retrieve prawler data from 2016 ITAE Bering Sea Mooring

"""
#System Stack
import datetime
import argparse

import wget

__author__   = 'Shaun Bell'
__email__    = 'shaun.bell@noaa.gov'
__created__  = datetime.datetime(2016, 6, 01)
__modified__ = datetime.datetime(2016, 6, 01)
__version__  = "0.1.0"
__status__   = "Development"
__keywords__ = 'CTD', 'SeaWater', 'Cruise', 'derivations'

"""--------------------------------helper Routines---------------------------------------"""


"""--------------------------------main Routines---------------------------------------"""

parser = argparse.ArgumentParser(description='NASA WorldView MODIS Retrieval')
parser.add_argument('doy', metavar='doy', type=str, help='Day of Year')               
parser.add_argument('sat_name', metavar='sat_name', type=str, help='Satellite Name (Aqua, Terra, Virrs)')               
parser.add_argument('format', metavar='format', type=str, help='(jpeg, png)')               
parser.add_argument('formatsize', metavar='formatsize', type=str, help='(small, large)')               
    
args = parser.parse_args()

### day of year to 3char string
if len(args.doy) == 1:
	doy = '00'+ args.doy
elif len(args.doy) == 2:
	doy = '0' + args.doy
else:
	doy = args.doy

dt = datetime.datetime(2016,1,1)
date_doy = (dt+datetime.timedelta(days=int(args.doy)-1.)).strftime('%Y%m%d')
filename = date_doy + '_' + args.formatsize + '.' + args.format
if args.format == 'jpeg':
	if args.formatsize == 'small':
		url = 'http://map2.vis.earthdata.nasa.gov/image-download?TIME=2016'+doy+'&extent=-2912099.9245392745,-998673.7005630452,-937827.9245392745,1786606.2994369548&epsg=3413&layers=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines&opacities=1,1&worldfile=false&format=image/jpeg&width=386&height=544'
	elif args.formatsize == 'large':
		url = 'http://map2.vis.earthdata.nasa.gov/image-download?TIME=2016'+doy+'&extent=-2912099.9245392745,-998673.7005630452,-937827.9245392745,1786606.2994369548&epsg=3413&layers=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines&opacities=1,1&worldfile=false&format=image/jpeg&width=1928&height=2720'
elif args.format == 'png':
	if args.formatsize == 'small':
		url = 'http://map2.vis.earthdata.nasa.gov/image-download?TIME=2016'+doy+'&extent=-2912099.9245392745,-998673.7005630452,-937827.9245392745,1786606.2994369548&epsg=3413&layers=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines&opacities=1,1&worldfile=false&format=image/png&width=386&height=544'
	elif args.formatsize == 'large':
		url = 'http://map2.vis.earthdata.nasa.gov/image-download?TIME=2016'+doy+'&extent=-2912099.9245392745,-998673.7005630452,-937827.9245392745,1786606.2994369548&epsg=3413&layers=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines&opacities=1,1&worldfile=false&format=image/png&width=1928&height=2720'

wget.download(url, filename, bar=wget.bar_thermometer)


