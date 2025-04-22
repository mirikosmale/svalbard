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

# sdv_aod_timeseries.py 2 2023 Svalbardcentre
# sdv_aod_timeseries.py 2 2023 Munich
# sdv_aod_timeseries.py 2 2023 Helsinki
# sdv_aod_timeseries.py 2 2023 Sodankyla

# sdv_aod_timeseries.py 0 20210801 20240531 Svalbardcentre
# sdv_aod_timeseries.py 0 20210801 20240531 Munich
# sdv_aod_timeseries.py 0 20210801 20240531 Helsinki
# sdv_aod_timeseries.py 0 20210801 20240531 Sodankyla

sdv_aod_timeseries.py 4 20210101 20211231 Svalbardcentre
sdv_aod_timeseries.py 4 20220101 20221231 Svalbardcentre
sdv_aod_timeseries.py 4 20230101 20231231 Svalbardcentre
# sdv_aod_timeseries.py 4 20240101 20241231 Svalbardcentre
sdv_aod_timeseries.py 4 20240401 20240430 Svalbardcentre
sdv_aod_timeseries.py 4 20240601 20240630 Svalbardcentre

# sdv_aod_timeseries.py 0 20210101 20211231 Munich
# sdv_aod_timeseries.py 0 20220101 20221231 Munich
# sdv_aod_timeseries.py 0 20230101 20231231 Munich
# sdv_aod_timeseries.py 0 20240101 20241231 Munich

# sdv_aod_timeseries.py 0 20210101 20211231 Helsinki
# sdv_aod_timeseries.py 0 20220101 20221231 Helsinki
# sdv_aod_timeseries.py 0 20230101 20231231 Helsinki
# sdv_aod_timeseries.py 0 20240101 20241231 Helsinki

# sdv_aod_timeseries.py 0 20210101 20211231 Sodankyla
# sdv_aod_timeseries.py 0 20220101 20221231 Sodankyla
# sdv_aod_timeseries.py 0 20230101 20231231 Sodankyla
# sdv_aod_timeseries.py 0 20240101 20241231 Sodankyla


# sdv_aod_timeseries.py 1 20210801 20240531 Svalbardcentre
# sdv_aod_timeseries.py 1 20210801 20240531 Munich
# sdv_aod_timeseries.py 1 20210801 20240531 Helsinki
# sdv_aod_timeseries.py 1 20210801 20240531 Sodankyla

# sdv_aod_timeseries.py 2 20210801 20240531 Svalbardcentre
# sdv_aod_timeseries.py 2 20210801 20240531 Munich
# sdv_aod_timeseries.py 2 20210801 20240531 Helsinki
# sdv_aod_timeseries.py 2 20210801 20240531 Sodankyla

# sdv_aod_timeseries.py 3 20210801 20240531 Svalbardcentre
# sdv_aod_timeseries.py 3 20210801 20240531 Munich
# sdv_aod_timeseries.py 3 20210801 20240531 Helsinki
# sdv_aod_timeseries.py 3 20210801 20240531 Sodankyla

# sdv_aod_timeseries.py 2 2024 Svalbardcentre
# sdv_aod_timeseries.py 2 2024 Munich
# sdv_aod_timeseries.py 2 2024 Helsinki
# sdv_aod_timeseries.py 2 2024 Sodankyla

# sdv_aod_timeseries.py 1 2024 Svalbardcentre
# sdv_aod_timeseries.py 1 2024 Munich
# sdv_aod_timeseries.py 1 2024 Helsinki
# sdv_aod_timeseries.py 1 2024 Sodankyla

# sdv_aod_timeseries.py 2 2022 Svalbardcentre
# sdv_aod_timeseries.py 2 2022 Munich
# sdv_aod_timeseries.py 2 2022 Helsinki
# sdv_aod_timeseries.py 2 2022 Sodankyla

# sdv_aod_timeseries.py 1 2022 Svalbardcentre
# sdv_aod_timeseries.py 1 2022 Munich
# sdv_aod_timeseries.py 1 2022 Helsinki
# sdv_aod_timeseries.py 1 2022 Sodankyla

