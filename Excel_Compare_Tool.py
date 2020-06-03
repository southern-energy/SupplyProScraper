import numpy as np
import pandas as pd
from datetime import datetime

previous_excel_sheet = str("2020-5-26-11_SPS_All_Builder_Tasks.xlsx")

todays_excel_sheet = str("2020-06-03-18_SPS_All_Builder_Tasks.xlsx")

old_excel_dataframe = pd.read_excel(previous_excel_sheet, sheetname=0, index_col=0, dtype=str)

print(old_excel_dataframe)

new_excel_dataframe = pd.read_excel(todays_excel_sheet, sheetname=0, index_col=0, dtype=str)

large_dataframe = old_excel_dataframe.append(new_excel_dataframe)

only_new_entries_dataframe = large_dataframe.drop_duplicates(keep=False)

print(only_new_entries_dataframe)

print("Current Month, Date & Time:" + str(datetime.now().month)+"-"+str(datetime.now().day)+str(datetime.now().hour))

now = str(str(datetime.today().strftime('%Y-%m-%d'))+"-"+str(datetime.now().hour))

only_new_entries_dataframe.to_excel(str(now) +"_Differences_Sheet.xlsx", index=False)

# only_new_entries_dataframe.to_excel("Differences_Sheet.xlsx", index=False)