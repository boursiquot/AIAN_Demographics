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

# # print "AI/AN Alone and in Combination (Unweighted)", aian_df["ALONE"].value_counts()

# print "AI/AN Alone and in Combination (Weighted N)", alone_group["PWGTP"].sum()

# print "AI/AN Alone and in Combination (Weighted %)",(alone_group["PWGTP"].sum()/aian_df["PWGTP"].sum())*100

# print "Mean Age by AI/AN Alone or Combination (Weighted)", aian_df.groupby("ALONE")["AGEP"].mean()

# print "Number of Health Insurance Plans (Unweighted)", (aian_df["HEALTH_INSURANCE_COUNT"].value_counts(sort = False)/aian_df["HEALTH_INSURANCE_COUNT"].value_counts(sort = False).sum())*100

# print "Number of Health Insurance Plans (Weighted)", (aian_df.groupby("HEALTH_INSURANCE_COUNT")["PWGTP"].sum()/aian_df["PWGTP"].sum())*100

# print "Top 5 States by AI/AN Alone or Combination (Unweighted)", aian_df.groupby(["ALONE","ST"])["ST"].count().groupby(level = 0, group_keys = False).nlargest(10)


# print "Top 5 States by AI/AN Alone or Combination (Weighted)", aian_df.groupby(["ALONE","ST"])["PWGTP"].sum().groupby(level = 0, group_keys = False).nlargest(5)



def counts ( var1, label):
	#print label, pd.crosstab(index = aian_df["ALONE"], columns = "var", margins = True )

	# print label, pd.crosstab(index = aian_df["ALONE"], columns = var1 , margins = True)	
	# var2 = (aian_df.groupby(["ALONE",var1])["PWGTP"].sum()/alone_group["PWGTP"].sum())*100.0

	# print label, (aian_df.groupby(["ALONE",var1])["PWGTP"].sum()/alone_group["PWGTP"].sum())*100.0
	print label, aian_df.groupby(["ALONE",var1])["PWGTP"].sum()
	

	nbase = aian_df[((aian_df["ALONE"] == 0) & (aian_df[var1] == 1))]
	dbase = aian_df[(aian_df["ALONE"] == 0)]

	n0 = nbase["PWGTP"].sum()
	d0 = dbase["PWGTP"].sum()

	# n0 = aian_df[((aian_df["ALONE"] == 0) & (aian_df[var1] == 1))]["PWGTP"].sum()
	# d0 = aian_df[(aian_df["ALONE"] == 0)]["PWGTP"].sum()

	print n0, d0

	nreps    = {}
	dreps    = {}
	nvalues  = []
	dvalues  = []
	

	nreps["n0"]  = n0
 	dreps["n0"]  = d0

	print nreps, dreps

	for w in rep_pwgtp:
	
		n = nbase[w].sum()
		ndiff = np.square((n - n0))
		nvalues.insert(0, n)
		nvalues.insert(1, ndiff)


		d = dbase[w].sum()
		ddiff = np.square((d - d0))
		dvalues.insert(0, d)
		dvalues.insert(1, ddiff)



		nreps[w] = nvalues
		dreps[w] = dvalues

		nvalues = []
		dvalues = []




	print "Numerator replicates", nreps, "Denominator replicates", dreps



	# print label, pd.crosstab(aian_df.ALONE, var2).apply(lambda r: (r/r.sum())*100, axis = 1)
	

counts ("DIS", "Disability Status (Weighted)")

# counts ("HINS4", "Medicaid Status (Weighted)")

# counts ("PUBCOV", "Public Health Insurance Status (Weighted)")

# counts ("PRIVCOV","Private Health Insurance Status (Weighted)")

# counts ("HICOV", "Health Insurance Status (Weighted)")

# counts ("HEALTH_INSURANCE_COUNT",  "Number of Health Insurance Plans (Weighted)")

# counts ("IHS", "Number of People Who List IHS as Insurance (Weighted)" )

# counts ("IHS_ALONE",  "Number of People with Only IHS as Insurance (Weighted)")


