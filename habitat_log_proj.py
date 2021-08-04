import pandas as pd
import numpy as np

logdf = pd.read_csv('Fall_2021_Points_Log.csv')
gmdf = pd.read_csv('GM_Sign_In_Responses.csv')

# drop Timestamp column
gmdf = gmdf.drop(['Timestamp'], axis = 1, inplace = False)
gmdf = gmdf.rename(columns = {'If you aren\'t on the newsletter and would like to stay up to date, enter your email below:':'newsletter',
                              'If this row has been visited, put at 1':'visited'})

gmdf.value_counts(gmdf['Last Name'])
# drop duplicate sign ins on GM sign in spreadsheet
# gmdf = gmdf.drop_duplicates(subset = 'Last Name')

# parse out the date from the timestamp and drop the time
gmdf['Timestamp'] = gmdf['Timestamp'].apply(lambda x: str(x).split(' ')[0])

# divide sign-ins by date. Use the first sign-in date as a benchmark and if the sign-in dates are within 3
# days of that benchmark date then put them into the same dataframe
type(gmdf['Timestamp'])

aggGMdf = gmdf.groupby(gmdf.Timestamp)

gmdf.columns
logdf.columns

# iterate through all the last names and add one to their GM points count
for i in range(len(gmdf['Last Name'])):
    #print(type(gmdf['visited'][i]))
    if gmdf['visited'][i] != 1:
        # look for all the empty "divider" lines in between GM days and ignore them so we can get right to the unvisited logs
        if gmdf['visited'][i-1] == 1 and gmdf['visited'][i+1] == 1:
            pass
        else:
            #print('the i value of ', i, ' is', gmdf['visited'][i])
            # check if last and first name at the index is in logdf 
            for j in range(len(logdf['Last Name'])):
                if (gmdf['Last Name'][i].lower().strip() == logdf['Last Name'][j].lower().strip()) and (gmdf['First Name '][i].lower().strip() == logdf['First Name'][j].lower().strip()):
                #if (gmdf['Last Name'][i] == logdf['Last Name'][j]) and (gmdf['First Name '][i] == logdf['First Name'][j]):
                    print(gmdf['Last Name'][i], " is matched by j value of ", j)
                    logdf['Meetings'] += 1

        
if (str(gmdf['Last Name'][0]) == str(logdf['Last Name'][0])):
    print(gmdf['Last Name'][0])
else:
    print('bagel')
