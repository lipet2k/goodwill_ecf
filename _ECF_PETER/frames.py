import pandas as pd

_file_name = 'facebook_research_act.xlsx'
_sheet_name = 'HDD'

data_df = pd.read_excel(_file_name, sheet_name=_sheet_name)

print(data_df)
