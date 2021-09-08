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
# if the newsletter has no '@' in it, then it isn't an email and we turn the cell into nan
gmdf['newsletter'] = gmdf['newsletter'].apply(lambda x: str(x) if '@' in str(x) else np.nan)

logdf['Last Name'] = logdf['Last Name'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())
logdf['First Name'] = logdf['First Name'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())
logdf['Email Address'] = logdf['Email Address'].apply(lambda x: x if pd.isnull(x) else str(x).lower().strip())

# iterate through all the last names and add one to their GM points count
for i in range(len(gmdf['Last Name'])):
    if gmdf['visited'][i] != 1:
        # look for all the empty "divider" lines in between GM days and ignore them so we can get right to the unvisited logs
        #if gmdf['visited'][i-1] == 1 and gmdf['visited'][i+1] == 1: pass
        # if the row in gmdf is nans, skip the row
        if pd.isnull(gmdf['First Name'][i]) and pd.isnull(gmdf['Last Name'][i]) and pd.isnull(gmdf['newsletter'][i]): continue
        else:
            # check if last and first name at the index is in logdf 
            for j in range(len(logdf['Last Name'])):
                if (gmdf['Last Name'][i] == logdf['Last Name'][j]) and (gmdf['First Name'][i] == logdf['First Name'][j]):
                    logdf['Meetings'][j] += 1
                    
                    # if the member has nan/no meeting points, assign the value to 1
                    if pd.isnull(logdf['Meetings'][j]): logdf['Meetings'][j] = 1
                    
                    # adds newsletter email into logdf if the cell isn't nan
                    if not pd.isnull(gmdf['newsletter'][i]): logdf['Email Address'][j] = gmdf['newsletter'][i]
            
            # checks logdf for Last Names in gmdf that don't exist yet
            for k in range(len(logdf['Last Name'])):
                if gmdf['Last Name'][i] not in logdf['Last Name'][k]: continue
                else: break
        
            # if the for loop reached the end of the Last Names in logdf, we know the gmdf Last Name has no match, so we append to the end of logdf
            if k == len(logdf['Last Name'])-1:
                # index for gmdf has to be same as the index of gmdf in the if statement
                df2 = {'Last Name': gmdf['Last Name'][i], 'First Name': gmdf['First Name'][i], 'Email Address': gmdf['newsletter'][i], 'Meetings': 1}   
                logdf = logdf.append(df2, ignore_index = True)
                break
      
# sort the dataframe alphabetically
logdf = logdf.sort_values('First Name')
                
                    
                
                
                
# a test of adding a new entry/member
#df3 = {'Last Name': 'juice', 'First Name': 'carrot', 'newsletter': 'carrotjuice@gmail.com'}
#gmdf = gmdf.append(df3, ignore_index = True)
