import numpy as np
import pandas as pd
import sys
import logging as lg
import time
import datetime as dt
import glob
# import xlsxwriter

#data_dict =  "http://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2011-2015.txt"

logname = "/Users/bernice/documents/ai_an/logs/reading_pums.log"

lg.basicConfig(filename = logname, level = lg.DEBUG, filemode = "w")

logger = lg.getLogger(__name__)

handler = logging.FileHandler

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


# # Code to get multirace counts and Excel workbook


aian = pd.DataFrame()
blk  = pd.DataFrame()
wht  = pd.DataFrame()
asn  = pd.DataFrame()
nhpi = pd.DataFrame()
sor  = pd.DataFrame()


# aian = acs11_15[(acs11_15["RACAIAN"] == 1)]
# blk  = acs11_15[(acs11_15["RACBLK"]  == 1)]
# wht  = acs11_15[(acs11_15["RACWHT"]  == 1)]
# asn  = acs11_15[(acs11_15["RACASN"]  == 1)]
# nhpi = acs11_15[(acs11_15["RACNHPI"] == 1)]
# sor  = acs11_15[(acs11_15["RACSOR"]  == 1)]

aian["Number"]  =  acs11_15[(acs11_15["RACAIAN"]  == 1)].groupby("RACNUM")["PWGTP"].sum()
blk["Number"]   =  acs11_15[(acs11_15["RACBLK"]   == 1)].groupby("RACNUM")["PWGTP"].sum()
wht["Number"]   =  acs11_15[(acs11_15["RACWHT"]   == 1)].groupby("RACNUM")["PWGTP"].sum()
asn["Number"]   =  acs11_15[(acs11_15["RACASN"]   == 1)].groupby("RACNUM")["PWGTP"].sum()
nhpi["Number"]  =  acs11_15[(acs11_15["RACNHPI"]  == 1)].groupby("RACNUM")["PWGTP"].sum()
sor["Number"]   =  acs11_15[(acs11_15["RACSOR"]   == 1)].groupby("RACNUM")["PWGTP"].sum()

aian["Percent"]  =  acs11_15[(acs11_15["RACAIAN"]  == 1)].groupby("RACNUM")["PWGTP"].sum()/(acs11_15[(acs11_15["RACAIAN"]  == 1)].groupby("RACNUM")["PWGTP"].sum()).sum()*100
blk["Percent"]   =  acs11_15[(acs11_15["RACBLK"]   == 1)].groupby("RACNUM")["PWGTP"].sum()/(acs11_15[(acs11_15["RACBLK"]   == 1)].groupby("RACNUM")["PWGTP"].sum()).sum()*100
wht["Percent"]   =  acs11_15[(acs11_15["RACWHT"]   == 1)].groupby("RACNUM")["PWGTP"].sum()/(acs11_15[(acs11_15["RACWHT"]   == 1)].groupby("RACNUM")["PWGTP"].sum()).sum()*100
asn["Percent"]   =  acs11_15[(acs11_15["RACASN"]   == 1)].groupby("RACNUM")["PWGTP"].sum()/(acs11_15[(acs11_15["RACASN"]   == 1)].groupby("RACNUM")["PWGTP"].sum()).sum()*100
nhpi["Percent"]  =  acs11_15[(acs11_15["RACNHPI"]  == 1)].groupby("RACNUM")["PWGTP"].sum()/(acs11_15[(acs11_15["RACNHPI"]  == 1)].groupby("RACNUM")["PWGTP"].sum()).sum()*100
sor["Percent"]   =  acs11_15[(acs11_15["RACSOR"]   == 1)].groupby("RACNUM")["PWGTP"].sum()/(acs11_15[(acs11_15["RACSOR"]   == 1)].groupby("RACNUM")["PWGTP"].sum()).sum()*100


# aian2  = aian.to_frame()
# blk2   = blk.to_frame()
# wht2   = wht.to_frame()
# asn2   = asn.to_frame()
# nhpi2  = nhpi.to_frame()
# sor2   = sor.to_frame()

# print  aian.groupby("RACNUM")["PWGTP"].sum()/aian.groupby("RACNUM")["PWGTP"].sum().sum()*100

# aian2.columns = ["AI AN Percent"]
# blk2.columns = ["Black Percent"]
# wht2.columns = ["White Percent"]
# asn2.columns = ["Asian Percent"]
# nhpi2.columns = ["Native Hawaiian Percent"]
# sor2.columns = ["Some Other Race Percent"]

# wkbk = xlsxwriter.Workbook("multirace_pop.xlsx")
# wkst = wkbk.add_worksheet()
# chst = wkbk.add_chartsheet()

writer  = pd.ExcelWriter("multirace_pop.xlsx", engine = "xlsxwriter")

aian.to_excel(writer, sheet_name = "AI_AN_Population")  
blk.to_excel(writer,  sheet_name = "Black_Population" ) 
wht.to_excel(writer,  sheet_name = "White_Population" ) 
asn.to_excel(writer,  sheet_name = "Asian_Popluation") 
nhpi.to_excel(writer, sheet_name = "Native_Hawaiian_Popluation") 
sor.to_excel(writer,  sheet_name = "Some_Other_Race_Population") 


writer.save()

# print "Number of observations", len(acs11_15.index)    

# Getting a df of AI/AN people

# pums11_15_aian  = acs11_15[(acs11_15["RACAIAN"] == 1)]

# print "Number of people who are AI/AN", acs11_15.loc[acs11_15["RACAIAN"] ==1, "PWGTP"].sum()

# # print "Number of people who are AI/AN", len(pums11_15_aian.index)


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

# print pums11_15_aian.sample(20)

# pums11_15_aian.to_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv")


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




# chst.add_series({"values": "=AI_AN Population!$B$2:$B$7"})
# chst.add_series({"values": "=Black Population!$B$2:$B$7"})
# chst.add_series({"values": "=White Population!$B$2:$B$7"})
# chst.add_series({"values": "=Asian Population!$B$2:$B$7"})
# chst.add_series({"values": "=Native Hawaiian Population!$B$2:$B$7"})
# chst.add_series({"values": "=Some Other Race!$B$2:$B$7"})





# # chart1 = wkbk.add_chart({"type": "bar"})

# # chart1.add_series({"name": "=Sheet1!$B$1", "categories": "=Sheet1!$A$2:$A$7", "values": "=Sheet1!$B$2:$B$7"})
# # chart1.add_series({"name": "=Sheet2!$B$1", "categories": "=Sheet2!$A$2:$A$7", "values": "=Sheet2!$B$2:$B$7"})
# # chart1.add_series({"name": "=Sheet3!$B$1", "categories": "=Sheet3!$A$2:$A$7", "values": "=Sheet3!$B$2:$B$7"})
# # chart1.add_series({"name": "=Sheet4!$B$1", "categories": "=Sheet4!$A$2:$A$7", "values": "=Sheet4!$B$2:$B$7"})
# # chart1.add_series({"name": "=Sheet5!$B$1", "categories": "=Sheet5!$A$2:$A$7", "values": "=Sheet5!$B$2:$B$7"})
# # chart1.add_series({"name": "=Sheet6!$B$1", "categories": "=Sheet6!$A$2:$A$7", "values": "=Sheet6!$B$2:$B$7"})

# # chart1.set_title({"name": "Number of Races"})
# # chart1.set_style(1)
# # chst.set_chart(chart1)

# # writer.save()
