#!/bin/bash
#=====#################################################################
# NAME:
#		set_system.sh
# CALLING SEQUENCE:
# 		source set_system.sh
# PURPOSE:
#		set the paths for the server
#		to ensure that all codes can be called easily
# AUTHOR:
#		written by Miriam Kosmale, 27.02.2020
# PROJECT:
#		Harvester Seasons
#
# INFO:
#		will be called in the beginning
#		or from each routine
#=====#################################################################



#=====#################################################################
# general settings
#=====#################################################################
# silentx=1 print no status
# silentx=0 print status
silentx=1
# if [ $silentx -eq 0 ] ; then  ; fi
#=====#################################################################
# system-dir 
#=====#################################################################
pathbase_working=/data/kosmale/svalbard
pathbase_dataserver=/litceph/GSdata
# pwddir=`pwd`
# projectpath=$pwddir
# echo $projectpath
[ -d ${pathbase_working} ] || mkdir -p ${pathbase_working}
#=====#################################################################
# algorithm sub-dirs for codes
#=====#################################################################
subpaths=(\
	"../add_login" \
	"../add_datadownload" \
	"settings" \
	"bash_code" \
	"python_code")
	
for subpath in "${subpaths[@]}"
do
pattern=$subpath && pwddir=$(pwd) && if [[ $pwddir =~ $pattern ]]; then projectpath=$(echo "$pwddir" | sed "s/\/$pattern//g") ; else projectpath=$pwddir; fi
done
addpath=${projectpath}
if [[ ":$PATH:" != *":$addpath:"* ]]; then
	export PATH=$PATH:$addpath
	[[ $silentx -eq 0 ]] && echo adding path $addpath
fi

# Code paths
for subpath in "${subpaths[@]}"
do
addpath=${projectpath}/${subpath}
if [[ ":$PATH:" != *":$addpath:"* ]]; then
	export PATH=$PATH:$addpath
	[[ $silentx -eq 0 ]] && echo adding path $addpath
fi
done

# Python paths
for subpath in "${subpaths[@]}"
do
addpath=${projectpath}/${subpath}
if [[ ":$PYTHONPATH:" != *":$addpath:"* ]]; then
	export PYTHONPATH=$PYTHONPATH:$addpath
	[[ $silentx -eq 0 ]] && echo adding path $addpath
fi
done

[[ $silentx -eq 0 ]] && echo $PATH | tr -s ':' '\n'

# echo pythonpaths-----------------
[[ $silentx -eq 0 ]] && echo $PYTHONPATH | tr -s ':' '\n'

#=====#################################################################
# end
#=====#################################################################

