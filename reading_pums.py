import numpy as np
import pandas as pd
import sys
import logging as lg
import time
import datetime as dt
import glob
import xlsxwriter

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

# Getting a df of AI/AN people

pums11_15_aian  = acs11_15[(acs11_15["RACAIAN"] == 1)]

# print "Number of people who are AI/AN", len(pums11_15_aian.index)


def alonemulti(row):
    if row["RAC1P"] == 3 or row["RAC1P"] == 4 or row["RAC1P"] == 5 or row["RAC3P05"] == 34 or row["RAC3P12"] == 3:
        row["ALONE"] = 1

    else:
         row["ALONE"] = 0

    return row



# # def hi_crosstab (var):

# #     print pd.crosstab(index = pums11_15_aian["HINS7"],  columns = var, margins = True)

# # hi_crosstab(pums11_15_aian["HINS1"])
# # hi_crosstab(pums11_15_aian["HINS2"])
# # hi_crosstab(pums11_15_aian["HINS3"])
# # hi_crosstab(pums11_15_aian["HINS4"])
# # hi_crosstab(pums11_15_aian["HINS5"])
# # hi_crosstab(pums11_15_aian["HINS6"])


def health_insurance (row):

    row["HEALTH_INSURANCE_COUNT"] = 0
    row["IHS"]   = 0
    row["IHS_ALONE"] = 0 

    if row["HINS1"] == 1 :
        row["HEALTH_INSURANCE_COUNT"] = row["HEALTH_INSURANCE_COUNT"] + 1
       
    if row["HINS2"] == 1 :
        row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

    if row["HINS3"] == 1 :
        row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

    if row["HINS4"] == 1 :
        row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

    if row["HINS5"] == 1 :
        row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

    if row["HINS6"] == 1 :
        row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1

    if row["HINS7"] == 1 :
        row["HEALTH_INSURANCE_COUNT"] =  row["HEALTH_INSURANCE_COUNT"] + 1
        row["IHS"]   = 1

    if row["HINS7"] == 1 and row["HINS1"] == 2  and row["HINS2"] == 2  and row["HINS3"] == 2  and row["HINS4"] == 2  and row["HINS5"] == 2 and row["HINS6"] == 2 :
        row["IHS_ALONE"] = 1

    return row


def disability (row):
    row["DISABILITY_COUNT"] = 0

    if row["DEYE"] == 1:
        row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

    if row["DEAR"] == 1:
        row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

    if row["DDRS"] == 1:
        row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

    if row["DOUT"] == 1:
        row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

    if row["DREM"] == 1:
        row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

    if row["DPHY"] == 1:
        row["DISABILITY_COUNT"] = row["DISABILITY_COUNT"] + 1

    return row



pums11_15_aian = pums11_15_aian.apply(alonemulti, axis = 1) ## axis = 0  apply function to each column, axis = 1 apply function to rows

print "ALONEMULTI function is complete"

pums11_15_aian = pums11_15_aian.apply(health_insurance, axis = 1) ## axis = 0  apply function to each column, axis = 1 apply function to rows

print "HEALTH_INSURANCE function is complete"

pums11_15_aian = pums11_15_aian.apply(disability, axis = 1) ## axis = 0  apply function to each column, axis = 1 apply function to rows

print "DISABILITY function is complete"

print pums11_15_aian.sample(20)

pums11_15_aian.to_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv")


end = dt.datetime.now().strftime("%Y/%m/%d %H:%M")


print "End time", end

# print "Time elapsed (sec) = {diff:1f}".format(diff = end - start)


# # Code to get multirace counts and Excel workbook

# aian = pd.DataFrame()
# blk  = pd.DataFrame()
# wht  = pd.DataFrame()
# asn  = pd.DataFrame()
# nhpi = pd.DataFrame()
# sor  = pd.DataFrame()


# aian = acs11_15[(acs11_15["RACAIAN"] == 1)]
# blk  = acs11_15[(acs11_15["RACBLK"] == 1)]
# wht  = acs11_15[(acs11_15["RACWHT"] == 1)]
# asn  = acs11_15[(acs11_15["RACASN"] == 1)]
# nhpi = acs11_15[(acs11_15["RACNHPI"] == 1)]
# sor  = acs11_15[(acs11_15["RACSOR"] == 1)]

# aian2 =  (aian["RACNUM"].value_counts()/aian["RACNUM"].value_counts().sum())*100
# blk2  =  (blk["RACNUM"].value_counts()/blk["RACNUM"].value_counts().sum())*100
# wht2  =  (wht["RACNUM"].value_counts()/wht["RACNUM"].value_counts().sum())*100
# asn2  =  (asn["RACNUM"].value_counts()/asn["RACNUM"].value_counts().sum())*100
# nhpi2  =  (nhpi["RACNUM"].value_counts()/nhpi["RACNUM"].value_counts().sum())*100
# sor2  =  (sor["RACNUM"].value_counts()/sor["RACNUM"].value_counts().sum())*100

# aian3  = aian2.to_frame()
# blk3   = blk2.to_frame()
# wht3   = wht2.to_frame()
# asn3   = asn2.to_frame()
# nhpi3  = nhpi2.to_frame()
# sor3   = sor2.to_frame()


# for i in (aian3, blk3, wht3, asn3, nhpi3, sor3):
#     i.columns = ["Percent"]


# writer  = pd.ExcelWriter("multirace_pop.xlsx", engine = "xlsxwriter")

# aian3.to_excel(writer, sheet_name = "AI_AN Population")  
# blk3.to_excel(writer,  sheet_name = "Black Population" ) 
# wht3.to_excel(writer,  sheet_name = "White Population" ) 
# asn3.to_excel(writer,  sheet_name =  "Asian Popluation") 
# nhpi3.to_excel(writer, sheet_name =  "Native Hawaiian Popluation") 
# sor3.to_excel(writer,  sheet_name =  "Some Other Race") 

# # wkbk  = writer.book
# # wksht = writer.sheets["AI_AN Population"] 
# # format1 = wkbk.add_format({"num_format":"0%"})
# # wksht = set_column("B:B",None, format1)

# writer.save()


