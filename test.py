import k_package as kp
import pandas as pd

df = pd.read_csv("test.csv") 
mycols = ["Matching time", "Alignment time"]
print("\nBEFORE\n")
print(df[mycols[0]].head()) 

km = kp.Kfun(df, mycols)
km.convert_all_time()

print("\nAFTER\n")    
print(km.dataframe[km.colnames[0]].head())