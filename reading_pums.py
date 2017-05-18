import numpy as np
import pandas as pd
import sys
import logging as lg
import time
import datetime as dt
import glob
# import xlsxwriter

#data_dict =  "http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2011-2015.txt"

start = dt.datetime.now().strftime("%Y/%m/%d %H:%M")

print "Start Time", start 

logname = "/Users/bernice/documents/ai_an/logs/reading_pums.log"

logger = lg.getLogger(__name__)
logger.setLevel(lg.DEBUG)

handler = lg.FileHandler(logname)
handler.setLevel(lg.DEBUG)

start = lg.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(start)

logger.addHandler(handler)

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

logger.info("ss15 csv files read")

# # Code to get multirace counts and Excel workbook

# acs11_15 = pd.read_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv", header = 0)

aian = pd.DataFrame()
blk  = pd.DataFrame()
wht  = pd.DataFrame()
asn  = pd.DataFrame()
nhpi = pd.DataFrame()
sor  = pd.DataFrame()

aian2 = pd.DataFrame()
blk2  = pd.DataFrame()
wht2  = pd.DataFrame()
asn2  = pd.DataFrame()
nhpi2 = pd.DataFrame()
sor2  = pd.DataFrame()

def racedfs (df, var, df2, title):
    df = acs11_15[(acs11_15[var] == 1)]
    logger.debug("%s data frame created", df)
    df["RACNUM_R"] = df.apply(lambda row: "3+" if row["RACNUM"] > 2 else str(int(row["RACNUM"])), axis = 1)
    print df.sample(25)
    new_group = df.groupby("RACNUM_R")
    
   
    df2["Number"] = new_group["PWGTP"].sum()
    df2["Percent"]   =  (new_group["PWGTP"].sum()/df["PWGTP"].sum())*100
    df2.loc["Group"] = title
   
    print df2
    logger.debug("Second %s data frame", df)
    
racedfs (aian,"RACAIAN", aian2, "American Indian/Alaska Native")
racedfs(blk, "RACBLK", blk2, "Black")
racedfs(wht, "RACWHT", wht2, "White")
racedfs(asn, "RACASN", asn2, "Asian")
racedfs(nhpi,"RACNHPI", nhpi2, "Native Hawaiian and Other Pacific Islander")
racedfs(sor, "RACSOR", sor2, "Some Other Race")


# print  aian.groupby("RACNUM")["PWGTP"].sum()/aian.groupby("RACNUM")["PWGTP"].sum().sum()*100


writer  = pd.ExcelWriter("/Users/bernice/documents/ai_an/output/multirace_pop.xlsx", engine = "xlsxwriter")

aian2.to_excel(writer, sheet_name = "AI_AN_Population")  
blk2.to_excel(writer,  sheet_name = "Black_Population" ) 
wht2.to_excel(writer,  sheet_name = "White_Population" ) 
asn2.to_excel(writer,  sheet_name = "Asian_Popluation") 
nhpi2.to_excel(writer, sheet_name = "Native_Hawaiian_Popluation") 
sor2.to_excel(writer,  sheet_name = "Some_Other_Race_Population") 


writer.save()

# print "Number of observations", len(acs11_15.index)    

# Getting a df of AI/AN people

# pums11_15_aian  = acs11_15[(acs11_15["RACAIAN"] == 1)]


# def alonemulti(row):
#     if row["RAC1P"] == 3 or row["RAC1P"] == 4 or row["RAC1P"] == 5 or row["RAC3P05"] == 34 or row["RAC3P12"] == 3:
#         row["ALONE"] = 1

#     else:
#          row["ALONE"] = 0

#     return row


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

# # print pums11_15_aian.sample(20)

# pums11_15_aian.to_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv")



end = lg.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(end)


end = dt.datetime.now().strftime("%Y/%m/%d %H:%M")

print "End time", end

# print "Time elapsed (sec) = {diff:1f}".format(diff = end - start)


# # def hi_crosstab (var):

# #     print pd.crosstab(index = pums11_15_aian["HINS7"],  columns = var, margins = True)

# # hi_crosstab(pums11_15_aian["HINS1"])
# # hi_crosstab(pums11_15_aian["HINS2"])
# # hi_crosstab(pums11_15_aian["HINS3"])
# # hi_crosstab(pums11_15_aian["HINS4"])
# # hi_crosstab(pums11_15_aian["HINS5"])
# # hi_crosstab(pums11_15_aian["HINS6"])




