# import libraries
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import h5py
import datetime
import pandas as pd
import datetime as dt
import datetime as dt

# https://medium.com/@gabrielagodinho/a-brief-tutorial-on-how-to-extract-a-time-series-from-multiple-he5-files-1b75382b5e5b
outpath='/home/users/kosmale'
caminho='/litceph/GSdata/G3P/org/amsr'
files=os.listdir(caminho)

files_he5=[f for f in files if f[-3:]=='he5']
files_he5


iuv_time_pd_ap = pd.DataFrame(columns=['date','lat','lon','swe_min','swe_max','swe_mean','swe_median'])
x=0
for i in files_he5:    
    f=h5py.File(caminho+'/'+files_he5[x],mode='r')
    some_string=files_he5[x]
    datexstr=some_string[-12:-4]
    for key in f.keys():
      print(key)
    PATH_NAME1='HDFEOS/GRIDS/Northern Hemisphere/Data Fields/'
    PATH_NAME='HDFEOS/GRIDS/Northern Hemisphere/'
    DATAFIELD_NAME=PATH_NAME1 + 'SWE_NorthernDaily'
    LAT_NAME=PATH_NAME + 'lat'
    LON_NAME=PATH_NAME + 'lon'
    dset=f[DATAFIELD_NAME]
    data0=dset[:]
    lat = f[LAT_NAME][:]
    lon = f[LON_NAME][:]
    _FillValue = dset.attrs['_FillValue']
    fa=float(_FillValue)
    data = data0.astype(np.float32)
    lat[lat == np.inf] = np.nan
    lon[lon == np.inf] = np.nan
    # Longyearbreen: 78.174442,15.484520
    lon_val=19.313383
    lat_val=79.078839
    # Svalbard: lat=79.078839,lon=19.313383
    dif_latitudes = np.abs(lat - lat_val)    
    dif_longitudes = np.abs(lon - lon_val)    
    distancias = np.sqrt(dif_latitudes**2 + dif_longitudes**2)    
    indice_mais_proximo = np.unravel_index(np.nanargmin(distancias), lat.shape)
    # indice_mais_proximo = np.unravel_index(np.nanmin(distancias), lat.shape)
    lat_mais_proxima = lat[indice_mais_proximo]
    lon_mais_proxima = lon[indice_mais_proximo]
    iuv_mais_proxima1 = data[indice_mais_proximo]
    # 78.127361,16.173997
    # lon_val=16.173997
    # lat_val=78.127361
    # dif_latitudes = np.abs(lat - lat_val)    
    # dif_longitudes = np.abs(lon - lon_val)    
    # distancias = np.sqrt(dif_latitudes**2 + dif_longitudes**2)    
    # indice_mais_proximo = np.unravel_index(np.nanargmin(distancias), lat.shape)
    # indice_mais_proximo = np.unravel_index(np.nanmin(distancias), lat.shape)
    # lat_mais_proxima = lat[indice_mais_proximo]
    # lon_mais_proxima = lon[indice_mais_proximo]
    # iuv_mais_proxima2 = data[indice_mais_proximo]
    # lon_val=14.584792
    # lat_val=77.876146
    # 77.876146,14.584792
    # dif_latitudes = np.abs(lat - lat_val)    
    # dif_longitudes = np.abs(lon - lon_val)    
    # distancias = np.sqrt(dif_latitudes**2 + dif_longitudes**2)    
    # indice_mais_proximo = np.unravel_index(np.nanargmin(distancias), lat.shape)
    # indice_mais_proximo = np.unravel_index(np.nanmin(distancias), lat.shape)
    # lat_mais_proxima = lat[indice_mais_proximo]
    # lon_mais_proxima = lon[indice_mais_proximo]
    # iuv_mais_proxima3 = data[indice_mais_proximo]
    # lon_val=16.233842
    # lat_val=78.212947
    # 78.212947,16.233842
    # dif_latitudes = np.abs(lat - lat_val)    
    # dif_longitudes = np.abs(lon - lon_val)    
    # distancias = np.sqrt(dif_latitudes**2 + dif_longitudes**2)    
    # indice_mais_proximo = np.unravel_index(np.nanargmin(distancias), lat.shape)
    # indice_mais_proximo = np.unravel_index(np.nanmin(distancias), lat.shape)
    # lat_mais_proxima = lat[indice_mais_proximo]
    # lon_mais_proxima = lon[indice_mais_proximo]
    # iuv_mais_proxima4 = data[indice_mais_proximo]
    # print(datexstr,lat_mais_proxima,lon_mais_proxima,iuv_mais_proxima1,iuv_mais_proxima2,iuv_mais_proxima3,iuv_mais_proxima4)
    ind=indice_mais_proximo
    nd=4
    data_svalbard=data[ind[0]-nd:ind[0]+nd,ind[1]-nd:ind[1]+nd]
    data_svalbard[data_svalbard > 241] = np.nan
    data_svalbard_min=np.nanmin(data_svalbard)
    data_svalbard_max=np.nanmax(data_svalbard)
    data_svalbard_median=np.nanmedian(data_svalbard)
    data_svalbard_mean=np.nanmean(data_svalbard)
    print(datexstr,lat_mais_proxima,lon_mais_proxima,data_svalbard_min,data_svalbard_max,data_svalbard_median,data_svalbard_mean)
    # x=x+1
    # datapd=str(datestr)
    # ['date','lat','lon','swe_min','swe_max','swe_mean','swe_median']
    iuv_time_pd = pd.DataFrame({'date': [datexstr],'lat': [lat_mais_proxima],'lon': [lon_mais_proxima],'swe_min': [data_svalbard_min],'swe_max': [data_svalbard_max],'swe_mean': [data_svalbard_mean],'swe_median': [data_svalbard_median]})
    iuv_time_pd_ap = iuv_time_pd_ap.append(iuv_time_pd, ignore_index=True)    
    directory_path = outpath
    file_name = 'amsr_swe_2025.csv'
    iuv_time_pd_ap.to_csv(directory_path +'/'+ file_name, index=True)
    x=x+1


iuv_time_pd_ap.date
dates=np.array([dt.datetime.strptime(str(i), '%Y%m%d') for i in iuv_time_pd_ap.date])
print(directory_path +'/'+ file_name)


df=iuv_time_pd_ap
df['dttime']=dates
df = df.sort_values(by='dttime')
date1=df.dttime.min()
date2=df.dttime.max()

name='AMSR'
datasetflag='SWE'
year1=2023
year2=2024
plotnamebase=directory_path+'/timeseries_'+'daily'+'_'+name+'_'+datasetflag+'_'+str(year1)+'_'+str(year2)+'_fullyear'
print(plotnamebase)

#---------------------------------
plt.figure()
year_title='winter '+str(year1)+'-'+str(year2)
title=name+' SWE '+year_title
ytitle='SWE'
fnameadd='v0'
fstr='%0.2f'
ylimit=[0., 100.]
data_col='b-'
data_col2='b-'
# plt.plot(df_loc.date.values,df_loc.swe_product.values,data_col, label="SWE ("+datasetflag+")", linestyle='-', marker='o')
plt.plot(df.dttime.values,df.swe_max.values,data_col, label="SWE [mm]", linestyle='None', marker='.')
print(plotnamebase+'.png')
plt.xlabel('date')
plt.gcf().autofmt_xdate()
ax = plt.gca()
# ax.set_xlim([year1, year2])
# date1_str=str(year1)+str(1).zfill(2)+str(1).zfill(2)
# date2_str=str(year2)+str(12).zfill(2)+str(31).zfill(2)
ax.set_xlim([dt.datetime.strptime(date1_str, '%Y%m%d'), dt.datetime.strptime(date2_str, '%Y%m%d')])
ax.set_xlim([date1, date2])
ax.grid(True)
ax.tick_params(rotation=30, axis='x')  # rotate xticks    
plt.grid(True) 
plt.title(title)
plt.ylabel(ytitle)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(fstr))
ax.set_ylim(ylimit)
# legend = ax.legend(loc='lower right', shadow=True, fontsize='medium')
legend = ax.legend(loc='upper right', shadow=True, fontsize='medium')
plt.tight_layout()  # otherwise the right y-label is slightly clipped
plotname=str(plotnamebase)+"_"+fnameadd+".png"
plt.savefig(plotname)
print('plotted: '+plotname)
#---------------------------------
plt.figure()
year_title='winter '+str(year1)+'-'+str(year2)
title=name+' SWE '+year_title
ytitle='SWE'
fnameadd='v1'
fstr='%0.2f'
ylimit=[0., 100.]
data_col='b-'
data_col2='c-'
# plt.plot(df_loc.date.values,df_loc.swe_product.values,data_col, label="SWE ("+datasetflag+")", linestyle='-', marker='o')
plt.plot(df.dttime.values,df.swe_max.values,data_col, label="SWE max [mm]", linestyle='None', marker='.')
plt.plot(df.dttime.values,df.swe_mean.values,data_col2, label="SWE mean [mm]", linestyle='None', marker='.')
# plt.plot(df.dttime.values,df.swe_max.values,data_col, label="SWE [mm]", linestyle='None', marker='.')
print(plotnamebase+'.png')
plt.xlabel('date')
plt.gcf().autofmt_xdate()
ax = plt.gca()
# ax.set_xlim([year1, year2])
# date1_str=str(year1)+str(1).zfill(2)+str(1).zfill(2)
# date2_str=str(year2)+str(12).zfill(2)+str(31).zfill(2)
ax.set_xlim([dt.datetime.strptime(date1_str, '%Y%m%d'), dt.datetime.strptime(date2_str, '%Y%m%d')])
ax.set_xlim([date1, date2])
ax.grid(True)
ax.tick_params(rotation=30, axis='x')  # rotate xticks    
plt.grid(True) 
plt.title(title)
plt.ylabel(ytitle)
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(fstr))
ax.set_ylim(ylimit)
# legend = ax.legend(loc='lower right', shadow=True, fontsize='medium')
legend = ax.legend(loc='upper right', shadow=True, fontsize='medium')
plt.tight_layout()  # otherwise the right y-label is slightly clipped
plotname=str(plotnamebase)+"_"+fnameadd+".png"
plt.savefig(plotname)
print('plotted: '+plotname)
