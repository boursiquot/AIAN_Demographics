import pandas as pd

aian_df = pd.read_csv("/Users/bernice/documents/ai_an/data/pums11_15_aian.csv", header = 0)

#print aian_df.sample(5)

print "Mean Age by AI/AN Alone or Combination", aian_df.groupby("ALONE")["AGEP"].mean()

print "Top 5 States by AI/AN Alone or Combination", aian_df.groupby(["ALONE","ST"])["ST"].count().groupby(level = 0, group_keys = False).nlargest(5)

