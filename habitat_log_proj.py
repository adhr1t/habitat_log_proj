import pandas as pd
import numpy as np

logdf = pd.read_csv('_____')
gmdf = pd.read_csv('_____')

# iterate through all the last names and add one to their GM points count
for i in range(len(gmdf['Last Name']))    :
    # check if last and first name at the index is in logdf 
    if gmdf['Last Name'][i] is in logdf['Last Name'][i] and gmdf['First Name'][i] is in logdf['First Name'][i]:
        logdf['General Meetings'] += 1
    
            
for i in gmdf['Last Name']:
    # check if last and first name at the index is in logdf 
    if gmdf['Last Name'] is in logdf['Last Name']:
        logdf['General Meetings'] += 1