import pandas as pd
import sys
import logging as lg
import time
import datetime as dt
import glob
import urllib2 as url
from bs4 import BeautifulSoup as bs
import re

#data_dict =  "http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2011-2015.txt"


start = dt.datetime.now().strftime("%Y/%m/%d %H:%M")

print "Start Time", start 

cols = ["serialno","SEX","AGEP","MAR","CIT","HINS1","HINS2","HINS3","HINS4","HINS5","HINS6","HINS7","RAC1P","RAC2P05","RAC2P12","RACAIAN","RAC3P05","RAC3P12","ST","PUMA10","PWGTP"]

csvs = glob.glob("/Users/bernice/documents/ai_an/data/ss15*.csv")

for i,f in enumerate(csvs):
    tempdf = pd.read_csv(f,header = 0,index_col = "serialno", usecols = cols )
    if i  == 0:
        acs11_15 = tempdf
    else:
        acs11_15 = acs11_15.append(tempdf)


#print "Time elapsed (sec) = diff:1f}".format(diff = end - start)

#print "Number of observations", len(acs11_15.index)    

## Getting a count of the number of AI/AN alone or in combination


# print "Variable RAC1P",  (acs11_15[(acs11_15["RAC1P"] == 3)  | (acs11_15["RAC1P"] == 4) | (acs11_15["RAC1P"] == 5) | (acs11_15["RAC3P05"] == 34) | (acs11_15["RAC3P12"] == 3)   
# | (acs11_15["RAC3P05"] == 33) | (acs11_15["RAC3P05"] == 35) | (acs11_15["RAC3P05"] == 43) 
# | (acs11_15["RAC3P05"] == 47) | (acs11_15["RAC3P05"] == 64) | (acs11_15["RAC3P05"] == 65) | (acs11_15["RAC3P05"] == 67)
# | (acs11_15["RAC3P12"] == 17) | (acs11_15["RAC3P12"] == 30) | (acs11_15["RAC3P12"] == 39) | (acs11_15["RAC3P12"] == 40) 
# | (acs11_15["RAC3P12"] == 41) | (acs11_15["RAC3P12"] == 60) | (acs11_15["RAC3P12"] == 63)| (acs11_15["RAC3P12"] == 64) 
# | (acs11_15["RAC3P12"] == 79) | (acs11_15["RAC3P12"] == 81) | (acs11_15["RAC3P12"] == 82)| (acs11_15["RAC3P12"] == 84) 
# | (acs11_15["RAC3P12"] == 90) | (acs11_15["RAC3P12"] == 92)]).count()

## Count is 312,208

pums11_15_aian  = acs11_15[(acs11_15["RAC1P"] == 3)  | (acs11_15["RAC1P"] == 4) | (acs11_15["RAC1P"] == 5) | (acs11_15["RAC3P05"] == 34) | (acs11_15["RAC3P12"] == 3)   
| (acs11_15["RAC3P05"] == 33) | (acs11_15["RAC3P05"] == 35) | (acs11_15["RAC3P05"] == 43) 
| (acs11_15["RAC3P05"] == 47) | (acs11_15["RAC3P05"] == 64) | (acs11_15["RAC3P05"] == 65) | (acs11_15["RAC3P05"] == 67)
| (acs11_15["RAC3P12"] == 17) | (acs11_15["RAC3P12"] == 30) | (acs11_15["RAC3P12"] == 39) | (acs11_15["RAC3P12"] == 40) 
| (acs11_15["RAC3P12"] == 41) | (acs11_15["RAC3P12"] == 60) | (acs11_15["RAC3P12"] == 63) | (acs11_15["RAC3P12"] == 64) 
| (acs11_15["RAC3P12"] == 79) | (acs11_15["RAC3P12"] == 81) | (acs11_15["RAC3P12"] == 82) | (acs11_15["RAC3P12"] == 84) 
| (acs11_15["RAC3P12"] == 90) | (acs11_15["RAC3P12"] == 92) ] 

print "Number of people who are AI/AN", len(pums11_15_aian.index)

## Need to create column for 0 = AI/AN alone and 1 = AI/AN multi


def alonemulti(row):
    if row["RAC1P"] == 3 or row["RAC1P"] == 4 or row["RAC1P"] == 5 or row["RAC3P05"] == 34 or row["RAC3P12"] == 3:
        row["ALONE"] = 1

    else:
         row["ALONE"] = 0

    return row

pums11_15_aian = pums11_15_aian.apply(alonemulti, axis = 1)

print pums11_15_aian.head()

pums11_15_aian.to_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv")


end = dt.datetime.now().strftime("%Y/%m/%d %H:%M")

print "End time", end





