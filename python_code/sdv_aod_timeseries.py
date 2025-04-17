#!/usr/bin/env python3
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, date2index
from scipy.io import netcdf #### <--- This is the library to import.
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
# from colorspace import diverging_hcl
import datetime
from copy import copy
import sys                
import pandas as pd
import matplotlib as mpl
import datetime as dt
import glob

import os

# nd_str=sys.argv[1]
# year1=sys.argv[2]
# date1_str=sys.argv[2]
# date2_str=sys.argv[3]
# locname=sys.argv[3]
nd_str=sys.argv[1]
date1_str=sys.argv[2]
date2_str=sys.argv[3]
locname=sys.argv[4]

outpath='/data/kosmale/svalbard/'
path='/litceph/GSdata/G3P/org/adv/SDV'
year1 = date1_str[0:4]
year2 = date2_str[0:4]
month1 = date1_str[4:6]
month2 = date2_str[4:6]
day1 = date1_str[6:8]
day2 = date2_str[6:8]
date1d=dt.date(int(year1), int( month1), int(day1))
date2d=dt.date(int(year2), int(month2), int(day2))
date1=int(date1_str)
date2=int(date2_str)
# yyyy=year1
# yyyy='2023'
# mm='04'
# dd='30'
# locname='Longyearbreen'
# year1 = date1_str[0:4]
# year2 = date2_str[0:4]
# month1 = date1_str[4:6]
# month1 = '01'
# month2 = date2_str[4:6]
# day1 = date1_str[6:8]
# day2 = date2_str[6:8]
# date1d=dt.date(int(year1), int( month1), int(day1))
# date2d=dt.date(int(year2), int(month2), int(day2))
# date1=int(date1_str)
# date2=int(date2_str)

# inpath=path+'/'+'L3/'+yyyy+'/'
pattern=path+'/'+'L3/*/*.nc'
files_nc = glob.glob(pattern)
# files=os.listdir(inpath)
# files_nc=[f for f in files if f[-2:]=='nc']
# files_year=[f for f in files_nc if f[0:4]==yyyy]



# Longyearbreen: 78.174442,15.484520
if locname == 'Longyearbreen':
    lon_val=15.484520
    lat_val=78.174442
    # Larsbren: lat=78.180212,lon=15.913168

if locname == 'Larsbren':
    lon_val=15.913168
    lat_val=78.180212
    # Spitzbergen centre: lat=79.078839,lon=19.3133

if locname == 'Svalbardcentre':
    lon_val=19.313383
    lat_val=79.078839
    # lat=79.078839,lon=19.313383

if locname == 'Helsinki':
    lon_val=24.945831
    lat_val=60.192059
    
if locname == 'Munich':
    lon_val=11.576124
    lat_val=48.13743000

if locname == 'Sodankyla':
    lon_val=26.6000
    lat_val=67.4167


# iuv_time_pd_ap = pd.DataFrame(columns=['date','lat','lon','aod'])
iuv_time_pd_ap = pd.DataFrame(columns=['date','lat','lon','aod_min','aod_max','aod_mean','aod_median'])

# fname=files_year[0]
variable='AOD550_mean'

x=0
# for fname in files_year:    
for fname in files_nc:    
    datexstr=fname[0:8]   
    datex=int(datexstr)
    x=x+1
    if datex < date1:
        continue
    if datex > date2:
        continue
    dataset = Dataset(inpath+fname,'r')
    # some_string=fname[0]
    var=np.array(dataset.variables[variable][:,:])
    lat = np.array(dataset.variables['latitude'][:])
    lon = np.array(dataset.variables['longitude'][:])
    
    dif_latitudes = np.abs(lat - lat_val)    
    dif_longitudes = np.abs(lon - lon_val)
    
    index_minlat = np.argmin(dif_latitudes)
    index_minlon = np.argmin(dif_longitudes)
    # distancias = np.sqrt(dif_latitudes**2 + dif_longitudes**2)    
    # indice_mais_proximo = np.unravel_index(np.nanargmin(distancias), lat.shape)
    # indice_mais_proximo = np.unravel_index(np.nanmin(distancias), lat.shape)
    lat_mais_proxima = lat[index_minlat]
    lon_mais_proxima = lon[index_minlon]
    nd=int(nd_str)
    if nd > 0:
        data_svalbard=var[index_minlat-nd:index_minlat+nd,index_minlon-nd:index_minlon+nd]
        data_svalbard[data_svalbard > 100] = np.nan
        data_svalbard[data_svalbard < 0] = np.nan
        data_svalbard_min=np.nanmin(data_svalbard)
        data_svalbard_max=np.nanmax(data_svalbard)
        data_svalbard_median=np.nanmedian(data_svalbard)
        data_svalbard_mean=np.nanmean(data_svalbard)
    else:
        data_svalbard=var[index_minlat,index_minlon]
        if varx > 100:
            varx= np.nan
        if varx < 0:
            varx= np.nan
        data_svalbard_min=data_svalbard
        data_svalbard_max=data_svalbard
        data_svalbard_median=data_svalbard
        data_svalbard_mean=data_svalbard


    print(datexstr,lat_mais_proxima,lon_mais_proxima,data_svalbard_min,data_svalbard_max,data_svalbard_median,data_svalbard_mean)
    # x=x+1
    # datapd=str(datestr)
    # ['date','lat','lon','swe_min','swe_max','swe_mean','swe_median']
    iuv_time_pd = pd.DataFrame({'date': [datexstr],'lat': [lat_mais_proxima],'lon': [lon_mais_proxima],'aod_min': [data_svalbard_min],'aod_max': [data_svalbard_max],'aod_mean': [data_svalbard_mean],'aod_median': [data_svalbard_median]})
    iuv_time_pd_ap = iuv_time_pd_ap.append(iuv_time_pd, ignore_index=True)    
    directory_path = outpath
    file_name = 'SDV_AOD_'+year1+'_'+locname+'.csv'
    iuv_time_pd_ap.to_csv(directory_path +'/'+ file_name, index=True)
   

iuv_time_pd_ap.date
dates=np.array([dt.datetime.strptime(str(i), '%Y%m%d') for i in iuv_time_pd_ap.date])
df=iuv_time_pd_ap
df['dttime']=dates
df = df.sort_values(by='dttime')
date1=df.dttime.min()
date2=df.dttime.max()

name='SDV'
datasetflag='AOD'
ymax=1.
ymin=0.

# file_name = 'amsr_swe_'+date1_str+'-'+date2_str+'_'+locname+'_nd'+str(nd)+'.csv'
# plotnamebase=outpath+'/timeseries_'+'daily'+'_'+name+'_'+datasetflag+'_'+str(year1)+'_'+str(year2)+'_'+periodname+'_nd'+str(nd)+'_'+locname
plotnamebase=outpath+'/timeseries_'+'daily'+'_'+name+'_'+datasetflag+'_'+date1_str+'-'+date2_str+'_'+locname+'_nd'+str(nd)+'_w0'
plotnamebase=outpath+'/timeseries_'+'daily'+'_'+name+'_'+datasetflag+'_'+date1_str+'-'+date2_str+'_'+locname+'_nd'+str(nd)
print(plotnamebase)


data_col='b-'
data_col2='g-'
data_col3='r-'
#---------------------------------
plt.figure()
year_title=date1_str+'-'+date2_str
title=name+' '+datasetflag+' '+year_title
ytitle=datasetflag
fnameadd='v00'
fstr='%0.2f'
ylimit=[ymin, ymax]
# plt.plot(df_loc.date.values,df_loc.swe_product.values,data_col, label="SWE ("+datasetflag+")", linestyle='-', marker='o')
# plt.plot(df.dttime.values,df.swe_max.values,data_col, label="SWE [mm]", linestyle='None', marker='.')
plt.plot(df.dttime.values,df.aod_median.values,data_col, label=datasetflag, linestyle='None', marker='.')
print(plotnamebase+'.png')
plt.xlabel('date')
plt.gcf().autofmt_xdate()
ax = plt.gca()

# ax.set_xlim([year1, year2])
# date1_str=str(year1)+str(1).zfill(2)+str(1).zfill(2)
# date2_str=str(year1)+str(12).zfill(2)+str(31).zfill(2)
ax.set_xlim([dt.datetime.strptime(date1_str, '%Y%m%d'), dt.datetime.strptime(date2_str, '%Y%m%d')])
# ax.set_xlim([date1, date2])
ax.grid(True)
ax.tick_params(rotation=30, axis='x')  # rotate xticks    
plt.grid(True) 
plt.title(title)
plt.ylabel(ytitle)
ax.yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter(fstr))
ax.set_ylim(ylimit)
# legend = ax.legend(loc='lower right', shadow=True, fontsize='medium')
legend = ax.legend(loc='upper right', shadow=True, fontsize='medium')
plt.tight_layout()  # otherwise the right y-label is slightly clipped
plotname=str(plotnamebase)+"_"+fnameadd+".png"
plt.savefig(plotname)
print('plotted: '+plotname)
#---------------------------------
plt.figure()
# year_title='winter '+str(year1)+'-'+str(year2)
title=name+' '+datasetflag+' '+year_title
ytitle=datasetflag
fnameadd='v00mean'
fstr='%0.2f'
ylimit=[ymin, ymax]
# plt.plot(df_loc.date.values,df_loc.swe_product.values,data_col, label="SWE ("+datasetflag+")", linestyle='-', marker='o')
plt.plot(df.dttime.values,df.aod_min.values,data_col2, label=datasetflag+" min", linestyle='None', marker='.')
plt.plot(df.dttime.values,df.aod_max.values,data_col3, label=datasetflag+" max", linestyle='None', marker='.')
plt.plot(df.dttime.values,df.aod_mean.values,data_col, label=datasetflag+" mean", linestyle='None', marker='.')
# plt.plot(df.dttime.values,df.swe_max.values,data_col, label="SWE [mm]", linestyle='None', marker='.')
print(plotnamebase+'.png')
plt.xlabel('date')
plt.gcf().autofmt_xdate()
ax = plt.gca()
# ax.set_xlim([year1, year2])
# date1_str=str(year1)+str(1).zfill(2)+str(1).zfill(2)
# date2_str=str(year2)+str(12).zfill(2)+str(31).zfill(2)
ax.set_xlim([dt.datetime.strptime(date1_str, '%Y%m%d'), dt.datetime.strptime(date2_str, '%Y%m%d')])
# ax.set_xlim([date1, date2])
ax.grid(True)
ax.tick_params(rotation=30, axis='x')  # rotate xticks    
plt.grid(True) 
plt.title(title)
plt.ylabel(ytitle)
ax.yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter(fstr))
ax.set_ylim(ylimit)
# legend = ax.legend(loc='lower right', shadow=True, fontsize='medium')
legend = ax.legend(loc='upper right', shadow=True, fontsize='medium')
plt.tight_layout()  # otherwise the right y-label is slightly clipped
plotname=str(plotnamebase)+"_"+fnameadd+".png"
plt.savefig(plotname)
print('plotted: '+plotname)
#---------------------------------
plt.figure()
# year_title='winter '+str(year1)+'-'+str(year2)
title=name+' '+datasetflag+' '+year_title
ytitle=datasetflag
fnameadd='v00median'
fstr='%0.2f'
ylimit=[ymin, ymax]
# plt.plot(df_loc.date.values,df_loc.swe_product.values,data_col, label="SWE ("+datasetflag+")", linestyle='-', marker='o')
plt.plot(df.dttime.values,df.aod_min.values,data_col2, label=datasetflag+" min", linestyle='None', marker='.')
plt.plot(df.dttime.values,df.aod_max.values,data_col3, label=datasetflag+" max", linestyle='None', marker='.')
plt.plot(df.dttime.values,df.aod_median.values,data_col, label=datasetflag+" median", linestyle='None', marker='.')
# plt.plot(df.dttime.values,df.swe_max.values,data_col, label="SWE [mm]", linestyle='None', marker='.')
print(plotnamebase+'.png')
plt.xlabel('date')
plt.gcf().autofmt_xdate()
ax = plt.gca()
# ax.set_xlim([year1, year2])
# date1_str=str(year1)+str(1).zfill(2)+str(1).zfill(2)
# date2_str=str(year2)+str(12).zfill(2)+str(31).zfill(2)
ax.set_xlim([dt.datetime.strptime(date1_str, '%Y%m%d'), dt.datetime.strptime(date2_str, '%Y%m%d')])
# ax.set_xlim([date1, date2])
ax.grid(True)
ax.tick_params(rotation=30, axis='x')  # rotate xticks    
plt.grid(True) 
plt.title(title)
plt.ylabel(ytitle)
ax.yaxis.set_major_formatter(mpl.ticker.FormatStrFormatter(fstr))
ax.set_ylim(ylimit)
# legend = ax.legend(loc='lower right', shadow=True, fontsize='medium')
legend = ax.legend(loc='upper right', shadow=True, fontsize='medium')
plt.tight_layout()  # otherwise the right y-label is slightly clipped
plotname=str(plotnamebase)+"_"+fnameadd+".png"
plt.savefig(plotname)
print('plotted: '+plotname)
