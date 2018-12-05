import pandas as pd
import matplotlib.pyplot as plt
'''Part 1'''
''' https://quickstats.nass.usda.gov/api/api_GET/?key=913F53CB-222B-3106-873F-CF044F6BDA6D&commodity_desc=TURKEYS&util_practice_desc=SLAUGHTER, FI&class_desc=YOUNG&statisticcat_desc=SLAUGHTERED&prodn_practice_desc=ALL PRODUCTION PRACTICES&unit_desc=HEAD&state_alpha=VA&year__GE=1989&format=CSV '''

'''Part 2'''
def convert_currency(val_series):
    """
        Convert the string number value to a integer
        - Remove commas
        - Convert to integer type
        """
    new_val = val.replace(',','')
    return int(new_val)
plt.style.use('classic')

'''Line plot for value(how many turkeys in each month)
    of each months btw 1989 - 2002 and 2009 - 2018'''


df_turkeys = pd.read_csv('download.csv', index_col='year')
#data["Salary"]= data["Salary"].astype(int)
convert_currency(df_turkeys.loc[2018])
df_turkeys_2018 = df_turkeys.loc[2018]
print(df_turkeys.loc[2018])

ax = plt.gca()
df_turkeys.Value=pd.to_numeric(df_turkeys.Value)

df_turkeys_2018.plot(kind='line',x='reference_period_desc',y='Value',ax=ax)
df_turkeys_2018.plot(kind='line',x='reference_period_desc',y='Value', color='red', ax=ax)

plt.show()
