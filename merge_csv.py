import pandas as pd
import os

df = pd.read_csv("./Sales_Data/Sales_April_2019.csv")

all_months_data = pd.DataFrame()

# returns a list of files in the Sales_Data directory
files = [file for file in os.listdir('./Sales_Data')]

for file in files:
    df = pd.read_csv("./Sales_Data/"+file)
    all_months_data = pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv", index=False)