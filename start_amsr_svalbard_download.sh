#=====#################################################################
# NAME:
#		start_amsr_svalbard_download.sh
# CALLING SEQUENCE:
#		start_amsr_svalbard_download.sh $year
#		start_amsr_svalbard_download.sh 2020
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

nsidc-donwload_SWE.py 20210501 20230430
