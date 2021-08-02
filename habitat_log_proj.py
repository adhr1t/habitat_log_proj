import pandas as pd
import numpy as np

logdf = pd.read_csv('Fall_2021_Points_Log.csv')
gmdf = pd.read_csv('GM_Sign_In_Responses.csv')

# drop Timestamp column
# gmdf = gmdf.drop(['Timestamp'], axis = 1, inplace = False)

gmdf.value_counts()
# drop duplicate sign ins on GM sign in spreadsheet
# gmdf = gmdf.drop_duplicates(subset = 'Last Name')

# parse out the date from the timestamp and drop the time
gmdf['Timestamp'] = gmdf['Timestamp'].apply(lambda x: str(x).split(' ')[0])

# divide sign-ins by date. Use the first sign-in date as a benchmark and if the sign-in dates are within 3
# days of that benchmark date then put them into the same dataframe
type(gmdf['Timestamp'])

aggGMdf = gmdf.groupby(gmdf.Timestamp)


while '''next row''' != np.nan():
    date = gmdf['Timestamp'].split()

# iterate through all the last names and add one to their GM points count
for i in range(len(gmdf['Last Name']))    :
    # check if last and first name at the index is in logdf 
    if gmdf['Last Name'][i] is in logdf['Last Name'][i] and gmdf['First Name'][i] is in logdf['First Name'][i]:
        logdf['General Meetings'] += 1
    
            
for i in gmdf['Last Name']:
    # check if last and first name at the index is in logdf 
    if gmdf['Last Name'] is in logdf['Last Name']:
        logdf['General Meetings'] += 1