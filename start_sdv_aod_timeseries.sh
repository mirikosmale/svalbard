#!/bin/bash
#=====#################################################################
# NAME:
#		start_sdv_svalbard_timeseries.sh
# CALLING SEQUENCE:
#		start_sdv_svalbard_timeseries.sh $year
#		start_sdv_svalbard_timeseries.sh 2020
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

sdv_aod_timeseries.py 2 2023 Svalbardcentre
sdv_aod_timeseries.py 2 2023 Munich
sdv_aod_timeseries.py 2 2023 Helsinki
sdv_aod_timeseries.py 2 2023 Sodankyla

sdv_aod_timeseries.py 1 2023 Svalbardcentre
sdv_aod_timeseries.py 1 2023 Munich
sdv_aod_timeseries.py 1 2023 Helsinki
sdv_aod_timeseries.py 1 2023 Sodankyla

sdv_aod_timeseries.py 2 2024 Svalbardcentre
sdv_aod_timeseries.py 2 2024 Munich
sdv_aod_timeseries.py 2 2024 Helsinki
sdv_aod_timeseries.py 2 2024 Sodankyla

sdv_aod_timeseries.py 1 2024 Svalbardcentre
sdv_aod_timeseries.py 1 2024 Munich
sdv_aod_timeseries.py 1 2024 Helsinki
sdv_aod_timeseries.py 1 2024 Sodankyla

sdv_aod_timeseries.py 2 2022 Svalbardcentre
sdv_aod_timeseries.py 2 2022 Munich
sdv_aod_timeseries.py 2 2022 Helsinki
sdv_aod_timeseries.py 2 2022 Sodankyla

sdv_aod_timeseries.py 1 2022 Svalbardcentre
sdv_aod_timeseries.py 1 2022 Munich
sdv_aod_timeseries.py 1 2022 Helsinki
sdv_aod_timeseries.py 1 2022 Sodankyla

