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

amsr_svalbard_timeseries.py