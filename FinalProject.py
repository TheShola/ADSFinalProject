import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''Part 1 of Final Project'''
'''API command used to get data'''
'''Copy and past link in any browser'''
''' https://quickstats.nass.usda.gov/api/api_GET/?key=913F53CB-222B-3106-873F-CF044F6BDA6D&
commodity_desc=TURKEYS&util_practice_desc=SLAUGHTER, FI&class_desc=YOUNG&
statisticcat_desc=SLAUGHTERED&prodn_practice_desc=ALL PRODUCTION PRACTICES&
unit_desc=HEAD&state_alpha=VA&year__GE=1989&format=CSV '''



'''Part 2 of Final Project'''
def convert_value(dataframe):
    """
        - Convert the string number value to a integer
        - Remove commas
        - Convert to integer type
        - Adds new column to dataframe with converted value
        """
    temp_list=[]
    for row_index, row in dataframe.iterrows():
        row['Value'] = row['Value'].replace(',','',2)
        row['Value'] = int(row['Value'])
        temp_list.append(row['Value'])
    dataframe['New_Value'] = temp_list
    return dataframe


'''Initialize Dataframe from csv (from above Part 1) with year column as index'''
df_turkeys = pd.read_csv('download.csv', index_col='year')

'''Convert Value column using convert_value'''
df_turkeys = convert_value(df_turkeys)

'''Drop rows of dataframe where reference_period_desc = 'year' '''
df_turkeys = df_turkeys[df_turkeys.New_Value<=10000000]


'''1989 DATA - MEAN AND MEDIAN'''
df_turkeys_1989 = df_turkeys.loc[1989]
print('1989')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1989['New_Value'].mean(), df_turkeys_1989['New_Value'].median()))

#  '''1990 DATA - MEAN AND MEDIAN'''
df_turkeys_1990 = df_turkeys.loc[1990]
print('1990')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1990['New_Value'].mean(), df_turkeys_1990['New_Value'].median()))

#  '''1991 DATA - MEAN AND MEDIAN'''
df_turkeys_1991 = df_turkeys.loc[1991]
print('1991')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1991['New_Value'].mean(), df_turkeys_1991['New_Value'].median()))

#  '''1992 DATA - MEAN AND MEDIAN'''
df_turkeys_1992 = df_turkeys.loc[1992]
print('1992')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1992['New_Value'].mean(), df_turkeys_1992['New_Value'].median()))

#  '''1993 DATA - MEAN AND MEDIAN'''
df_turkeys_1993 = df_turkeys.loc[1993]
print('1993')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1993['New_Value'].mean(), df_turkeys_1993['New_Value'].median()))

#  '''1994 DATA - MEAN AND MEDIAN'''
df_turkeys_1994 = df_turkeys.loc[1994]
print('1994')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1994['New_Value'].mean(), df_turkeys_1994['New_Value'].median()))


#  '''1995 DATA - MEAN AND MEDIAN'''
df_turkeys_1995 = df_turkeys.loc[1995]
print('1995')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1995['New_Value'].mean(), df_turkeys_1995['New_Value'].median()))

#  '''1996 DATA - MEAN AND MEDIAN'''
df_turkeys_1996 = df_turkeys.loc[1996]
print('1996')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1996['New_Value'].mean(), df_turkeys_1996['New_Value'].median()))


#  '''1997 DATA - MEAN AND MEDIAN'''
df_turkeys_1997 = df_turkeys.loc[1997]
print('1997')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1997['New_Value'].mean(), df_turkeys_1997['New_Value'].median()))


#  '''1998 DATA - MEAN AND MEDIAN'''
df_turkeys_1998 = df_turkeys.loc[1998]
print('1998')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1998['New_Value'].mean(), df_turkeys_1998['New_Value'].median()))

#  '''1999 DATA - MEAN AND MEDIAN'''
df_turkeys_1999 = df_turkeys.loc[1999]
print('1999')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_1999['New_Value'].mean(), df_turkeys_1999['New_Value'].median()))


#  '''2000 DATA - MEAN AND MEDIAN'''
df_turkeys_2000 = df_turkeys.loc[2000]
print('2000')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2000['New_Value'].mean(), df_turkeys_2000['New_Value'].median()))

#  '''2001 DATA - MEAN AND MEDIAN'''
df_turkeys_2001 = df_turkeys.loc[2001]
print('2001')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2001['New_Value'].mean(), df_turkeys_2001['New_Value'].median()))

#  '''2002 DATA - MEAN AND MEDIAN'''
df_turkeys_2002 = df_turkeys.loc[2002]
print('2002')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2002['New_Value'].mean(), df_turkeys_2002['New_Value'].median()))

#  '''2009 DATA - MEAN AND MEDIAN'''
df_turkeys_2009 = df_turkeys.loc[2009]
print('2009')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2009['New_Value'].mean(), df_turkeys_2009['New_Value'].median()))

#  '''2010 DATA- MEAN AND MEDIAN'''
df_turkeys_2010 = df_turkeys.loc[2010]
print('2010')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2010['New_Value'].mean(), df_turkeys_2010['New_Value'].median()))

#  '''2011 DATA - MEAN AND MEDIAN'''
df_turkeys_2011 = df_turkeys.loc[2011]
print('2011')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2011['New_Value'].mean(), df_turkeys_2011['New_Value'].median()))

#  '''2012 DATA - MEAN AND MEDIAN'''
df_turkeys_2012 = df_turkeys.loc[2012]
print('2012')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2012['New_Value'].mean(), df_turkeys_2012['New_Value'].median()))

#  '''2013 DATA - MEAN AND MEDIAN'''
df_turkeys_2013 = df_turkeys.loc[2013]
print('2013')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2013['New_Value'].mean(), df_turkeys_2013['New_Value'].median()))

#  '''2014 DATA - MEAN AND MEDIAN'''
df_turkeys_2014 = df_turkeys.loc[2014]
print('2014')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2014['New_Value'].mean(), df_turkeys_2014['New_Value'].median()))

#  '''2015 DATA - MEAN AND MEDIAN'''
df_turkeys_2015 = df_turkeys.loc[2015]
print('2015')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2015['New_Value'].mean(), df_turkeys_2015['New_Value'].median()))

#  '''2016 DATA - MEAN AND MEDIAN'''
df_turkeys_2016 = df_turkeys.loc[2016]
print('2016')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2016['New_Value'].mean(), df_turkeys_2016['New_Value'].median()))

#  '''2017 DATA - MEAN AND MEDIAN'''
df_turkeys_2017 = df_turkeys.loc[2017]
print('2017')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2017['New_Value'].mean(), df_turkeys_2017['New_Value'].median()))

#  '''2018 DATA - MEAN AND MEDIAN'''
df_turkeys_2018 = df_turkeys.loc[2018]
print('2018')
print("Mean\t\tMedian")
print("%.2f\t%i \n" % (df_turkeys_2018['New_Value'].mean(), df_turkeys_2018['New_Value'].median()))


'''Line plots for value(how many turkeys in each month) of each months btw 1989 - 2002'''

plt.figure(1)
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1989, marker='', color='red', linewidth=1, label="1989")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1990, marker='', color='blue', linewidth=1, label="1990")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1991, marker='', color='olive', linewidth=1, label="1991")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1992, marker='', color='yellow', linewidth=1, label="1992")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1993, marker='', color='orange', linewidth=1, label="1993")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1994, marker='o', markerfacecolor='blue', 
    markersize=12, color='skyblue', linewidth=1, label="1994")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1995, marker='', color='red', 
    linewidth=1, linestyle='dashed', label="1995")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1996, marker='o', markerfacecolor='black', 
    markersize=8, color='black', linewidth=1, label="1996")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1997, marker='o', markerfacecolor='red', 
    markersize=8, color='red', linewidth=1, label="1997")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1998, marker='', color='magenta', 
    linewidth=1, linestyle='-.', label="1998")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1999, marker='', color='grey', 
    linewidth=1, linestyle='dashed', label="1999")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2000, marker='', color='magenta', linewidth=1, label="2000")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1999, marker='', color='orange', 
    linewidth=1, linestyle='-.', label="2001")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_1999, marker='', color='grey', 
    linewidth=1, linestyle='-.', label="2002")
plt.legend(loc=0)
plt.xlabel('Months')
plt.ylabel('Value of Turkeys ')
plt.title("Line plots for value(how many turkeys in each month) of each months btw 1989 - 2002")


'''Line plots for value(how many turkeys in each month) of each months btw 2009 - 2018'''

plt.figure(2)
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2009, marker='', color='red', linewidth=1, label="2009")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2010, marker='', color='blue', linewidth=1, label="2010")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2011, marker='', color='olive', linewidth=1, label="2011")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2012, marker='', color='yellow', linewidth=1, label="2012")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2013, marker='', color='orange', linewidth=1, label="2013")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2014, marker='o', markerfacecolor='blue', 
    markersize=12, color='skyblue', linewidth=1, label="2014")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2015, marker='', color='red', 
    linewidth=1, linestyle='dashed', label="2015")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2016, marker='o', markerfacecolor='black', 
    markersize=8, color='black', linewidth=1, label="2016")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2017, marker='o', markerfacecolor='red', 
    markersize=8, color='red', linewidth=1, label="2017")
plt.plot( 'reference_period_desc', 'New_Value', data=df_turkeys_2018, marker='', color='magenta', 
    linewidth=1, linestyle='dashed', label="2018")

plt.legend(loc=0)
plt.xlabel('Months')
plt.ylabel('Value of Turkeys ')
plt.title("Line plots for value(how many turkeys in each month) of each months btw 2009 - 2018")

plt.show()


