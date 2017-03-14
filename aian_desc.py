import pandas as pd

aian_df = pd.read_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv", header = 0)

# print aian_df.sample(5)

print "AI/AN Alone and in Combination", aian_df["ALONE"].value_counts()
# print "Mean Age by AI/AN Alone or Combination", aian_df.groupby("ALONE")["AGEP"].mean()

# print "Top 5 States by AI/AN Alone or Combination", aian_df.groupby(["ALONE","ST"])["ST"].count().groupby(level = 0, group_keys = False).nlargest(5)

def counts (var1 , var2, label):
	#print label, pd.crosstab(index = aian_df["ALONE"], columns = "var", margins = True )

	print label, pd.crosstab(index = aian_df["ALONE"], columns = var1 , margins = True)	
	print label, pd.crosstab(aian_df.ALONE, var2).apply(lambda r: (r/r.sum())*100, axis = 1)
	

counts (aian_df["DIS"], aian_df.DIS, "Disability Status")

counts (aian_df["HINS4"], aian_df.PUBCOV, "Medicaid Status")

counts (aian_df["PUBCOV"], aian_df.PUBCOV, "Public Health Insurance Status")

counts (aian_df["PRIVCOV"], aian_df.PRIVCOV, "Private Health Insurance Status")

counts (aian_df["HICOV"], aian_df.HICOV, "Private Health Insurance Status")
