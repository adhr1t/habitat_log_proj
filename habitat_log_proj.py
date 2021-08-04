import pandas as pd
import numpy as np

gmdf = pd.read_csv('GM_Sign_In_Responses.csv')
logdf = pd.read_csv('Fall_2021_Points_Log.csv')

# drop Timestamp column
gmdf = gmdf.drop(['Timestamp'], axis = 1, inplace = False)
gmdf = gmdf.rename(columns = {'If you aren\'t on the newsletter and would like to stay up to date, enter your email below:':'newsletter',
                              'If this row has been visited, put at 1':'visited', 'First Name ':'First Name'})

# lower and strip the first and last names of gmdf and logdf
gmdf['Last Name'] = gmdf['Last Name'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())
gmdf['First Name'] = gmdf['First Name'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())
gmdf['newsletter'] = gmdf['newsletter'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())

logdf['Last Name'] = logdf['Last Name'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())
logdf['First Name'] = logdf['First Name'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())
logdf['Email Address'] = logdf['Email Address'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())


# iterate through all the last names and add one to their GM points count
for i in range(len(gmdf['Last Name'])):
    if gmdf['visited'][i] != 1:
        # look for all the empty "divider" lines in between GM days and ignore them so we can get right to the unvisited logs
        if gmdf['visited'][i-1] == 1 and gmdf['visited'][i+1] == 1:
            pass
        else:
            # check if last and first name at the index is in logdf 
            for j in range(len(logdf['Last Name'])):
                if (gmdf['Last Name'][i] == logdf['Last Name'][j]) and (gmdf['First Name'][i] == logdf['First Name'][j]):
                    #print(gmdf['Last Name'][i], " is matched by j value of ", j)   # this prints the index of matched names
                    logdf['Meetings'][j] += 1
