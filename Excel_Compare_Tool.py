import numpy as np
import pandas as pd

old_excel_dataframe = pd.read_excel("OldSupplyProOutput.xlsx", sheetname=0, index_col=0, dtype=str)

print(old_excel_dataframe)

new_excel_dataframe = pd.read_excel("NewSupplyProOutput.xlsx", sheetname=0, index_col=0, dtype=str)

large_dataframe = old_excel_dataframe.append(new_excel_dataframe)

only_new_entries_dataframe = large_dataframe.drop_duplicates(keep=False)

print(only_new_entries_dataframe)

only_new_entries_dataframe.to_excel("Differences_Sheet.xlsx", index=False)