import pandas as pd
import glob

csv_file = glob.glob("*.csv")

full_data = pd.read_csv("Hotel_DaNang_Processed.csv")
for csv in csv_file[1:]:
    data = pd.read_csv(csv)
    full_data = pd.concat((full_data,data),axis=0,ignore_index=True)

full_data.to_csv("Full_Hotel.csv")
