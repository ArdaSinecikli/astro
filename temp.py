# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import astropy.io.fits as fits  
#from astropy.table import Table 
#from astropy.utils.data import get_pkg_data_filename
from astropy.timeseries import TimeSeries
import matplotlib.pyplot as plt
from pathlib import Path

star_directory = r"Stars" #The directory where you place your star light curves

#loops over ^^ directory and plots out every .fits light curve thats in there.
pathlist = Path(star_directory).glob('**/*.fits') #specifies whcih format to read.
for path in pathlist:
    
    path_in_str = str(path)   #..needed because path is object not string

    ts = TimeSeries.read(path_in_str, format='kepler.fits') #reads the file
    
    
    fig, ax = plt.subplots() #standard matplotlib stuff.
    ax.plot(ts.time.jd, ts['sap_flux'], 'k.', markersize=1)
    ax.set(xlabel='Julian Date', ylabel='SAP Flux (e-/s)')
    plt.show()



#some snippets I used previously but not anymore. could be useful.

#this one opens a fits file and gets info from it such as rows and columns. 
#Need to print to actually show it.
'''
#filename = 'whatever you want'

tmp = fits.open(path_in_str) 

tmp.info()
'''
 
#this one reads the .fits file and prints out the rows, columns an its contents.
#Gets truncated during print because its so large.
'''
from astropy.table import Table 

data = Table.read('tess2024300212641-s0085-0000000010164865-0282-s_lc.fits') 

print(data) #actually prints the data.  
'''

#this one reads the .fits file and saves it as a .ecsv file
#I decided against using it since astropy can read fits files anyways
'''
    tmp = fits.open(path_in_str) 
    tmp.info() 
    data = Table.read(path_in_str) 
    print(data)
    data.write('values.ecsv', overwrite=True)
'''