import pandas as pd
import sys
import logging as lg
import time
import datetime as dt
import glob
import urllib2 as url
from bs4 import BeautifulSoup as bs
import re

data_dict =  "http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2011-2015.txt"


start = dt.datetime.now().strftime("%Y/%m/%d %H:%M")

print "Start Time", start 

cols = ["sex","agep","cit","hins1","hins2","hins3","hins4","hins5","hins6","hins7","rac1p","rac2p05","rac2p12","racaian","rac3p05","rac3p12","st","puma10","pwgtp"]

csvs = glob.glob("/Users/bernice/documents/ai_an/data/ss15*.csv")

for i,f in enumerate(csvs):
    tempdf = pd.read_csv(f,header = 0, usecols = [c.upper()for c in cols])
    if i  == 0:
        acs11_15 = tempdf
    else:
        acs11_15 = acs11_15.append(tempdf,ignore_index = True)



end = dt.datetime.now().strftime("%Y/%m/%d %H:%M")

print "End time", end

#print "Time elapsed (sec) = diff:1f}".format(diff = end - start)
 
print acs11_15.head()

print "Number of observations", len(acs11_15.index)

pums11_15_aian_alone = acs11_15[(acs11_15["RAC1P"] == 3) | (acs11_15["RAC1P"] == 4) | (acs11_15["RAC1P"] == 5) | (acs11_15["RAC3P05"] == 34) | (acs11_15["RAC3P12"] == 3)  ] 

pums11_15_aian_multi = acs11_15[(acs11_15["RAC3P05"] == 33)   | (acs11_15["RAC3P05"] == 35) | (acs11_15["RAC3P05"] == 43) 
| (acs11_15["RAC3P05"] == 47) | (acs11_15["RAC3P05"] == 64) | (acs11_15["RAC3P05"] == 65) | (acs11_15["RAC3P05"] == 67)
| (acs11_15["RAC3P12"] == 17) | (acs11_15["RAC3P12"] == 30) | (acs11_15["RAC3P12"] == 39) | (acs11_15["RAC3P12"] == 40) 
| (acs11_15["RAC3P12"] == 41) | (acs11_15["RAC3P12"] == 60) | (acs11_15["RAC3P12"] == 63)| (acs11_15["RAC3P12"] == 64) 
| (acs11_15["RAC3P12"] == 79) | (acs11_15["RAC3P12"] == 81) | (acs11_15["RAC3P12"] == 82)| (acs11_15["RAC3P12"] == 84) 
| (acs11_15["RAC3P12"] == 90) | (acs11_15["RAC3P12"] == 92) ] 

print "Number of people who are AI/AN alone", len(pums11_15_aian_alone.index)
print "Number of people who are AI/AN and another race", len(pums11_15_aian_multi.index)

#pums11_15_aian_alone.to_csv("/Users/bernice/documents/ai_an/data/ss15pus_aian_alone.csv",index = False)

#pums11_15_aian_multi.to_csv("/Users/bernice/documents/ai_an/data/ss15pus_aian_multi.csv",index = False)


