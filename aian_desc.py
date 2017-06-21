from __future__ import division
import pandas as pd
import numpy as np


rep_pwgtp = []

for i in range(1,81):
    var = "PWGTP"+str(i)
    rep_pwgtp.append(var)


aian_df = pd.read_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv", header = 0)

# print aian_df.sample(25)

alone_group = aian_df.groupby("ALONE")

# print aian_df.columns.values


# print "AI/AN Total Population",aian_df["PWGTP"].sum()

# print "AI/AN Alone and in Combination (Unweighted)", aian_df["ALONE"].value_counts()

# print "AI/AN Alone and in Combination (Weighted N)", alone_group["PWGTP"].sum()

# print "AI/AN Alone and in Combination (Weighted %)",(alone_group["PWGTP"].sum()/aian_df["PWGTP"].sum())*100

# print "Mean Age by AI/AN Alone or Combination (Weighted)", aian_df.groupby("ALONE")["AGEP"].mean()

# print "IHS (Unweighted)", (aian_df["IHS_ALONE"].value_counts(sort = False)/aian_df["IHS_ALONE"].value_counts(sort = False).sum())*100

# print "IHS (Weighted)", (aian_df.groupby("IHS_ALONE")["PWGTP"].sum()/aian_df["PWGTP"].sum())*100


# print "Number of Health Insurance Plans (Unweighted)", (aian_df["HEALTH_INSURANCE_COUNT"].value_counts(sort = False)/aian_df["HEALTH_INSURANCE_COUNT"].value_counts(sort = False).sum())*100

# print "Number of Health Insurance Plans (Weighted)", (aian_df.groupby("HEALTH_INSURANCE_COUNT")["PWGTP"].sum()/aian_df["PWGTP"].sum())*100

# print "Top 5 States by AI/AN Alone or Combination (Unweighted)", aian_df.groupby(["ALONE","ST"])["ST"].count().groupby(level = 0, group_keys = False).nlargest(10)


# print "Top 5 States by AI/AN Alone or Combination (Weighted)", aian_df.groupby(["ALONE","ST"])["PWGTP"].sum().groupby(level = 0, group_keys = False).nlargest(5)



def counts (var1, label):

	nsum = 0 
	dsum = 0

	j = 0

	nbase = aian_df.groupby(["ALONE",var1])
	cross = nbase["PWGTP"].sum()
	print cross
	x = list(cross)

	while j < len(x):
		for i in x:

	
			# nbase = aian_df[((aian_df["ALONE"] == 0) & (aian_df[var1] == 1))]
			# dbase = aian_df[(aian_df["ALONE"] == 0)]


			n0 = i
			print "Current base estimate", n0
			# d0 = dbase["PWGTP"].sum()

			nsum = 0 
			print "Reset nsum"

			for w in rep_pwgtp:
	
				n = list(nbase[w].sum())[j]  ## Applying weight
				print "Weighted estimate", n
				ndiff = np.square((n - n0))  ## Getting squared difference between [w] estimate and [0] estimat


				# d = dbase[w].sum()  ## Applying weight
				# ddiff = np.square((d - d0))  ## Getting squared difference between [w] estimate and [0] estimate

				nsum = nsum + ndiff 
				print nsum

				# Exit rep_pwgtp for loop 

				# dsum = dsum + ddiff
				

			nse = np.sqrt((4/80) * nsum)
		# dse = np.sqrt((4/80) * dsum)

			nmoe = nse * 1.645

			print "SE",nse, "Estimate", n0, "MOE", nmoe

			j = j + 1

			print j

	# dmoe = dse * 1.645

	# print label, pd.crosstab(index = aian_df["ALONE"], columns = aian_df[var1] , margins = True)	
	
	# print label, (aian_df.groupby(["ALONE",var1])["PWGTP"].sum()/alone_group["PWGTP"].sum()) * 100.0
	# print label, aian_df.groupby(["ALONE",var1])["PWGTP"].sum()



# counts ("DIS", "Disability Status (Weighted)")

# counts ("HINS4", "Medicaid Status (Weighted)")

# counts ("PUBCOV", "Public Health Insurance Status (Weighted)")

# counts ("PRIVCOV","Private Health Insurance Status (Weighted)")

# counts ("HICOV", "Health Insurance Status (Weighted)")

counts ("HEALTH_INSURANCE_COUNT",  "Number of Health Insurance Plans (Weighted)")

# counts ("IHS", "Number of People Who List IHS as Insurance (Weighted)" )

# counts ("IHS_ALONE",  "Number of People with Only IHS as Insurance (Weighted)")


