#!/bin/sh

datapath='/Volumes/WDC_internal/Users/bell/in_and_outbox/2016/wood/ArcticHeat/sep/'


#AXCTD's

#9/10
python ArcticHeatCTD_stats.py ${datapath}AH20160910_data/AH20160910_ax/16037895_2016_09_10_20_50_44.ed.xlsx -axctd --maxdepth 985 -bd 
python ArcticHeatCTD_stats.py ${datapath}AH20160910_data/AH20160910_ax/16037899_2016_09_10_23_38_03.ed.xlsx -axctd --maxdepth 88 -bd

#9/11
#python ArcticHeatCTD_stats.py ${datapath}AH20160911_data/AH20160911_ax/16037897_2016_09_11_19_36_03.dta -axctd --maxdepth 39 

#9/15
python ArcticHeatCTD_stats.py ${datapath}AH20160915_data/AH20160915_ax/16037896_2016_09_15_21_31_25.ed.xlsx -axctd --maxdepth 43 -bd
python ArcticHeatCTD_stats.py ${datapath}AH20160915_data/AH20160915_ax/16037898_2016_09_15_22_33_45.ed.xlsx -axctd --maxdepth 42 -bd
