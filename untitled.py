import numpy as np
import pandas as pd
import sys
import logging as lg
import time
import datetime as dt
import glob
import xlsxwriter

start = dt.datetime.now().strftime("%Y/%m/%d %H:%M")

print "Start Time", start 

# Getting replicate weight variables in a list

rep_pwgtp = []

for i in range(1,81):
    var = "PWGTP"+str(i)
    rep_pwgtp.append(var)


cols = ["serialno","SEX","AGEP","MAR","CIT","DIS","DEYE","DEAR","DDRS","DOUT","DPHY","DREM","HICOV","PRIVCOV","PUBCOV","HINS1",
"HINS2","HINS3","HINS4","HINS5","HINS6","HINS7","RAC1P","RAC2P05","RAC2P12","RAC3P05","RAC3P12","RACAIAN","RACBLK","RACASN",
"RACNHPI","RACSOR","RACWHT","RACNUM","HISP","ST","PUMA00","PUMA10","PWGTP"]

cols.extend(rep_pwgtp)


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

aian = pd.DataFrame()
blk  = pd.DataFrame()
wht  = pd.DataFrame()
asn  = pd.DataFrame()
nhpi = pd.DataFrame()
sor  = pd.DataFrame()
