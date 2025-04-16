#!/bin/bash
#=====#################################################################
# NAME:
#		start_amsr_svalbard_timeseries.sh
# CALLING SEQUENCE:
#		start_amsr_svalbard_timeseries.sh $year
#		start_amsr_svalbard_timeseries.sh 2020
# PURPOSE:
#		
# NEEDS:
#		
# AUTHOR:
#		written by Miriam Kosmale, 03.03.2025
# PROJECT:
#
# INFO:
#		
#=====#################################################################
source set_system.sh
source /data/kosmale/venv/bin/activate

amsr_svalbard_timeseries.py 2 20230801 20240730 Svalbardcentre
amsr_svalbard_timeseries.py 2 20240801 20250730 Svalbardcentre
amsr_svalbard_timeseries.py 2 20230401 20250730 Svalbardcentre

amsr_svalbard_timeseries.py 1 20230801 20240730 Svalbardcentre
amsr_svalbard_timeseries.py 1 20240801 20250730 Svalbardcentre
amsr_svalbard_timeseries.py 1 20230401 20250730 Svalbardcentre

amsr_svalbard_timeseries.py 4 20230801 20240730 Svalbardcentre
amsr_svalbard_timeseries.py 4 20240801 20250730 Svalbardcentre
amsr_svalbard_timeseries.py 4 20230401 20250730 Svalbardcentre

amsr_svalbard_timeseries.py 2 20230801 20240730 Larsbren
amsr_svalbard_timeseries.py 2 20240801 20250730 Larsbren
amsr_svalbard_timeseries.py 2 20230401 20250730 Larsbren

amsr_svalbard_timeseries.py 2 20230801 20240730 Longyearbreen
amsr_svalbard_timeseries.py 2 20240801 20250730 Longyearbreen
amsr_svalbard_timeseries.py 2 20230401 20250730 Longyearbreen
