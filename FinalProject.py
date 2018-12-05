import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''Part 1'''
''' https://quickstats.nass.usda.gov/api/api_GET/?key=913F53CB-222B-3106-873F-CF044F6BDA6D&commodity_desc=TURKEYS&util_practice_desc=SLAUGHTER, FI&class_desc=YOUNG&statisticcat_desc=SLAUGHTERED&prodn_practice_desc=ALL PRODUCTION PRACTICES&unit_desc=HEAD&state_alpha=VA&year__GE=1989&format=CSV '''

'''Part 2'''
"""Remove outliers"""
def remove_outliers(dataframe):
    for row_index, row in dataframe.iterrows():
        if(dataframe['New_Value'].mean() - row['New_Value'] >= 10000000):
            dataframe.drop([row_index])
    return dataframe

def convert_value(val_df):
    temp_list=[]
    """
        Convert the string number value to a integer
        - Remove commas
        - Convert to integer type
        """
    for row_index, row in val_df.iterrows():
        row['Value'] = row['Value'].replace(',','',2)
        row['Value'] = int(row['Value'])
        temp_list.append(row['Value'])
    val_df['New_Value'] = temp_list
    return val_df
'''Dataframe'''
df_turkeys = pd.read_csv('download.csv', index_col='year')
df_turkeys = convert_value(df_turkeys)
'''2009 DATA'''
df_turkeys_2009 = df_turkeys.loc[2009]
df_turkeys_2009= df_turkeys_2009[df_turkeys_2009.New_Value<=10000000]
'''2010 DATA'''
df_turkeys_2010 = df_turkeys.loc[2010]
df_turkeys_2010= df_turkeys_2010[df_turkeys_2010.New_Value<=10000000]
'''2011 DATA'''
df_turkeys_2011 = df_turkeys.loc[2011]
df_turkeys_2011= df_turkeys_2011[df_turkeys_2011.New_Value<=10000000]
'''2011 DATA'''
df_turkeys_2011 = df_turkeys.loc[2011]
df_turkeys_2011= df_turkeys_2011[df_turkeys_2011.New_Value<=10000000]
print(df_turkeys_2009)
print(df_turkeys_2010)



'''Line plot for value(how many turkeys in each month)
    of each months btw 1989 - 2002 and 2009 - 2018'''

sns.set(style="darkgrid")
'''2009 PLOT'''
sns.lineplot(x='reference_period_desc', y='New_Value', sort=False,
             data=df_turkeys_2009)
'''2010 PLOT'''
sns.lineplot(x='reference_period_desc', y='New_Value', sort=False,
             data=df_turkeys_2010)
'''2011 PLOT'''
sns.lineplot(x='reference_period_desc', y='New_Value', sort=False,
             data=df_turkeys_2011)

plt.show()



