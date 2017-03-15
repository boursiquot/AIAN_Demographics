import csv
import numpy as np
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

cols = ["serialno","SEX","AGEP","MAR","CIT","DIS","DEYE","DEAR","DDRS","DOUT","DPHY","DREM","HICOV","PRIVCOV","PUBCOV","HINS1",
"HINS2","HINS3","HINS4","HINS5","HINS6","HINS7","RAC1P","RAC2P05","RAC2P12","RAC3P05","RAC3P12","RACAIAN","RACBLK","RACASN",
"RACNHPI","RACSOR","RACWHT","RACNUM","HISP","ST","PUMA00","PUMA10","PWGTP"]

csvs = glob.glob("/Users/bernice/documents/ai_an/data/ss15*.csv")

for i,f in enumerate(csvs):
    tempdf = pd.read_csv(f,header = 0,index_col = "serialno", usecols = cols, dtype ={
	    	"AGEP": int,"SEX": int, "DOUT" : str, "serialno" : int,"MAR" : int,"CIT" : int,"DIS" : int,"DEYE" : int
	        ,"DEAR" : int,"DDRS" : str,"DOUT" : str,"DPHY" : str,"DREM" : str,"HICOV" : int,"PRIVCOV" : int
	        ,"PUBCOV" : int,"HINS1" : int, "HINS2" : int, "HINS3" : int,"HINS4" : int,"HINS5" : int,"HINS6" : int
	        ,"HINS7" : int,"RAC1P" : int,"RAC2P05" : int,"RAC2P12" : int,"RACAIAN" : int,"RAC3P05" : int,"RAC3P12" : int
	        ,"RACAIAN" : int, "RACBLK" : int, "RACASN" : int, "RACNHPI" : int, "RACSOR" : int, "RACWHT" : int, "RACNUM" : int
	        , "HISP" : int, "ST" : int, "PUMA00" : str, "PUMA10" : str } )
    if i  == 0:
        acs11_15 = tempdf
    else:
        acs11_15 = acs11_15.append(tempdf)


# print acs11_15.head(5)

# print "Number of observations", len(acs11_15.index)    

# print type(len(acs11_15.index))


# multirace_num = acs11_15["RACNUM"].value_counts()

# multirace_pct = (acs11_15["RACNUM"].value_counts()/acs11_15["RACNUM"].value_counts().sum())*100

#print "Number of multirace people", multirace_num, multirace_pct, multirace_blk

def mr (var, title):
    new_df = acs11_15[(acs11_15[var] == 1)]
    print title, (new_df["RACNUM"].value_counts()/new_df["RACNUM"].value_counts().sum())*100

mr("RACBLK", "Number of Races Indicated Among Black Population")

mr("RACAIAN", "Number of Races Indicated Among American Indian and Alaska Native Population")

mr("RACWHT", "Number of Races Indicated Among White Population")

mr("RACASN", "Number of Races Indicated Among Asian Population")

mr("RACSOR", "Number of Races Indicated Among Some Other Race Population")

# # Getting a count of the number of AI/AN alone or in combination


# print "Variable RAC1P",  (acs11_15[(acs11_15["RAC1P"] == 3)  | (acs11_15["RAC1P"] == 4) | (acs11_15["RAC1P"] == 5) | (acs11_15["RAC3P05"] == 34) | (acs11_15["RAC3P12"] == 3)   
# | (acs11_15["RAC3P05"] == 33) | (acs11_15["RAC3P05"] == 35) | (acs11_15["RAC3P05"] == 43) 
# | (acs11_15["RAC3P05"] == 47) | (acs11_15["RAC3P05"] == 64) | (acs11_15["RAC3P05"] == 65) | (acs11_15["RAC3P05"] == 67)
# | (acs11_15["RAC3P12"] == 17) | (acs11_15["RAC3P12"] == 30) | (acs11_15["RAC3P12"] == 39) | (acs11_15["RAC3P12"] == 40) 
# | (acs11_15["RAC3P12"] == 41) | (acs11_15["RAC3P12"] == 60) | (acs11_15["RAC3P12"] == 63)| (acs11_15["RAC3P12"] == 64) 
# | (acs11_15["RAC3P12"] == 79) | (acs11_15["RAC3P12"] == 81) | (acs11_15["RAC3P12"] == 82)| (acs11_15["RAC3P12"] == 84) 
# | (acs11_15["RAC3P12"] == 90) | (acs11_15["RAC3P12"] == 92)]).count()

# Count is 312,208

# pums11_15_aian  = acs11_15[(acs11_15["RACAIAN"] == 1)]

# acs11_15[(acs11_15["RAC1P"] == 3)  | (acs11_15["RAC1P"] == 4) | (acs11_15["RAC1P"] == 5) | (acs11_15["RAC3P05"] == 34) | (acs11_15["RAC3P12"] == 3)   
# | (acs11_15["RAC3P05"] == 33) | (acs11_15["RAC3P05"] == 35) | (acs11_15["RAC3P05"] == 43) 
# | (acs11_15["RAC3P05"] == 47) | (acs11_15["RAC3P05"] == 64) | (acs11_15["RAC3P05"] == 65) | (acs11_15["RAC3P05"] == 67)
# | (acs11_15["RAC3P12"] == 17) | (acs11_15["RAC3P12"] == 30) | (acs11_15["RAC3P12"] == 39) | (acs11_15["RAC3P12"] == 40) 
# | (acs11_15["RAC3P12"] == 41) | (acs11_15["RAC3P12"] == 60) | (acs11_15["RAC3P12"] == 63) | (acs11_15["RAC3P12"] == 64) 
# | (acs11_15["RAC3P12"] == 79) | (acs11_15["RAC3P12"] == 81) | (acs11_15["RAC3P12"] == 82) | (acs11_15["RAC3P12"] == 84) 
# | (acs11_15["RAC3P12"] == 90) | (acs11_15["RAC3P12"] == 92) ] 

# print "Number of people who are AI/AN", len(pums11_15_aian.index)


# def alonemulti(row):
#     if row["RAC1P"] == 3 or row["RAC1P"] == 4 or row["RAC1P"] == 5 or row["RAC3P05"] == 34 or row["RAC3P12"] == 3:
#         row["ALONE"] = 1

#     else:
#          row["ALONE"] = 0

#     return row



# # def hi_crosstab (var):

# #     print pd.crosstab(index = pums11_15_aian["HINS7"],  columns = var, margins = True)

# # hi_crosstab(pums11_15_aian["HINS1"])
# # hi_crosstab(pums11_15_aian["HINS2"])
# # hi_crosstab(pums11_15_aian["HINS3"])
# # hi_crosstab(pums11_15_aian["HINS4"])
# # hi_crosstab(pums11_15_aian["HINS5"])
# # hi_crosstab(pums11_15_aian["HINS6"])


# def health_insurance (row):

#     row["HEALTH_INSURANCE_COUNT"] = 0
#     row["IHS"]   = 0
#     row["IHS_ALONE"] = 0 

#     if row["HINS1"] == 1 :
#         row["HEALTH_INSURANCE_COUNT"] = row["HEALTH_INSURANCE_COUNT"] + 1
       
#     if row["HINS2"] == 1 :
#         row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

#     if row["HINS3"] == 1 :
#         row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

#     if row["HINS4"] == 1 :
#         row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

#     if row["HINS5"] == 1 :
#         row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

#     if row["HINS6"] == 1 :
#         row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

#     if row["HINS7"] == 1 :
#         row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1
#         row["IHS"]   = 1

#     if row["HINS7"] == 1 and row["HINS1"] == 2  and row["HINS2"] == 2  and row["HINS3"] == 2  and row["HINS4"] == 2  and row["HINS5"] == 2 and row["HINS6"] == 2 :
#         row["IHS_ALONE"] = 1

#     return row


# def disability (row):
#     row["DISABILITY_COUNT"] = 0

#     if row["DEYE"] == 1:
#         row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

#     if row["DEAR"] == 1:
#         row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

#     if row["DDRS"] == 1:
#         row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

#     if row["DOUT"] == 1:
#         row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

#     if row["DREM"] == 1:
#         row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

#     if row["DPHY"] == 1:
#         row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

#     return row



# pums11_15_aian = pums11_15_aian.apply(alonemulti, axis = 1) ## axis = 0  apply function to each column, axis = 1 apply function to rows

# print "ALONEMULTI function is complete"

# pums11_15_aian = pums11_15_aian.apply(health_insurance, axis = 1) ## axis = 0  apply function to each column, axis = 1 apply function to rows

# print "HEALTH_INSURANCE function is complete"

# pums11_15_aian = pums11_15_aian.apply(disability, axis = 1) ## axis = 0  apply function to each column, axis = 1 apply function to rows

# print "DISABILITY function is complete"

# pums11_15_aian.to_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv")

# print pums11_15_aian.sample(20)

end = dt.datetime.now().strftime("%Y/%m/%d %H:%M")


print "End time", end
# print "Time elapsed (sec) = {diff:1f}".format(diff = end - start)





