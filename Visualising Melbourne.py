import numpy as np
import pandas as pd
import seaborn as sns

street_furniture = pd.read_csv('./Data/Street_furniture_including_bollards__bicycle_rails__bins__drinking_fountains__horse_troughs__planter_boxes__seats__barbecues.csv')
trees = pd.read_csv('./Data/Trees__with_species_and_dimensions__Urban_Forest_.csv')
resources = pd.read_csv('./Data/Environmental_resources_consumed__including_air_travel__chemicals__electricity__fuel__gas__water__and_waste_generated_2013-14.csv')
pedestrians = pd.read_csv('./Data/Pedestrian_volume__updated_monthly_.csv')


street_furniture.dtypes
street_furniture.head(30)
street_furniture.columns

#check nulls in LOCATION_DESC
street_furniture['LOCATION_DESC'].isnull().sum()

#fix missing location
column = 'LOCATION_DESC'
for index, row in street_furniture[column].iteritems():
        if (pd.isnull(street_furniture.loc[index,column])):
            street_furniture.loc[index,column] = 'Melbourne' 

for index, row in street_furniture[column].iteritems():
    location = street_furniture.loc[index,column]
    if(',' in location):
       stringsplit = location.split(',')
       street_furniture.loc[index,'Area'] = stringsplit[len(stringsplit) - 2].strip()
    else:
       street_furniture.loc[index,'Area'] = 'Melbourne'

f, ax = plt.subplots(figsize=(20, 10))
sns.countplot(y='Area', data=street_furniture)

f, ax = plt.subplots(figsize=(20, 10))
sns.countplot(y='ASSET_TYPE', data=street_furniture)

#Condition Rating
f, ax = plt.subplots(figsize=(20, 10))
sns.pointplot(x="Area", y="CONDITION_RATING", data=street_furniture);

#Trees
trees.head(100)
trees.columns
trees['Precinct'].isnull().sum()

f, ax = plt.subplots(figsize=(20, 10))
sns.countplot(y='Precinct', data=trees)

#Resources 
resources.head(100)
resources.columns
sns.kdeplot(resources['Total Greenhouse Gases (t CO2-e)'])
em = resources.groupby('Branch')['Total Greenhouse Gases (t CO2-e)'].mean()
sns.distplot(em, kde=False);
sns.pointplot(x="Total Greenhouse Gases (t CO2-e)", y="Branch",  data=resources);

#Pedestrians
pedestrians.head()

pedestrians_avg = pedestrians.groupby('Year').Hourly_Counts.mean()
f, ax = plt.subplots(figsize=(20, 10))
sns.tsplot(data=pedestrians_avg)

pedestrians_avg = pedestrians.groupby('Day').Hourly_Counts.mean()
f, ax = plt.subplots(figsize=(20, 10))
sns.pointplot(x="Day", y="Hourly_Counts", data=pedestrians)
