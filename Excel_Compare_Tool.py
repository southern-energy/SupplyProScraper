import numpy as np
import pandas as pd
from datetime import datetime

previous_excel_sheet = str("2020-12-07-16_SPS_All_Builder_Tasks.xlsx")

todays_excel_sheet = str("2020-12-14-10_SPS_All_Builder_Tasks.xlsx")

old_excel_dataframe = pd.read_excel(previous_excel_sheet, sheet_name=0, dtype=str)

old_excel_dataframe["Old_Sheet"] = True

print(old_excel_dataframe)

new_excel_dataframe = pd.read_excel(todays_excel_sheet, sheet_name=0, dtype=str)

new_excel_dataframe["Old_Sheet"] = False

large_dataframe = old_excel_dataframe.append(new_excel_dataframe)

only_new_entries_dataframe = large_dataframe.drop_duplicates(subset=['Account', 'Job', 'Subdivision', 'Lot /Block', 'Task /PO Contract Date','TaxAmount', 'JobSubtotal(Excl Tax)', 'Total'], keep=False)


print(only_new_entries_dataframe.columns)

print("Current Month, Date & Time:" + str(datetime.now().month)+"-"+str(datetime.now().day)+str(datetime.now().hour))

now = str(str(datetime.today().strftime('%Y-%m-%d'))+"-"+str(datetime.now().hour))

only_new_entries_dataframe.to_excel(str(now) +"_Differences_Sheet.xlsx", index=False)

# only_new_entries_dataframe.to_excel("Differences_Sheet.xlsx", index=False)