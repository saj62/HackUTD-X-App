import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

df = pd.read_csv('/Users/zora/desktop/datasets/natural_disasters/us_disaster_declarations.csv')
df.head(10)

df.info()

sns.pairplot(df[['disaster_number','fy_declared','incident_type','declaration_request_number']])

disaster_types = df['incident_type'].unique()
print("Types of Disasters reported:\n\n", disaster_types)
print("Occurrences:\n\n",df['incident_type'].value_counts())

plt.pyplot.figure(figsize=(10,6))
sns.distplot(df['incident_type'].value_counts())

m=df[['fy_declared','incident_type']].groupby('fy_declared').describe()['incident_type'].reset_index()
plt.pyplot.figure(figsize=(9,6))
sns.barplot(x='top',y='freq',data =m)

m=df['fy_declared'].value_counts().reset_index()
m.head(10)

sns.lmplot(x='fy_declared',y='count',data=m.sort_values(by='fy_declared'),
           aspect=1.7, height=5,markers=['o'], scatter_kws={'s':20})

m=df[['state','incident_type']].groupby('state').describe()
m['incident_type'].sort_values(by='count',ascending=False).head(10)


m=df[['state','incident_type']].groupby('state').describe()
sns.pairplot(m['incident_type'].reset_index(drop=True))

m['incident_type'].sort_values(by='freq',ascending=False)['freq'].head(10)

p = df[['state','incident_type']].groupby('state').count()
p.reset_index(inplace=True)
p=p.sort_values(by='incident_type',ascending=False).head(10)
p

plt.pyplot.figure(figsize=(16,8))
sns.barplot(x="state", y="incident_type", data=p,)

print("Texas mostly faces:\n")
df[['state','incident_type']].groupby('state').max().loc['TX']

m=df.query('state=="TX"')['fy_declared'].value_counts().reset_index()
m.head(10)

plt.pyplot.figure(figsize=(24,12))
sns.barplot(x='fy_declared',y='count',data=m.sort_values(by='fy_declared'));

df.query('state == "TX" & fy_declared=="2020"')['incident_type'].unique()

print("Total Areas\n",df['designated_area'].nunique())

df[['designated_area','incident_type']].groupby('designated_area').count().sort_values(by='incident_type',ascending=False).head(10)

d = pd.to_datetime(df['declaration_date']).dt
df['year'] = d.year
df['month'] = d.month
df['day'] = d.day
df['time'] = d.time
del df['declaration_date']

df['declaration_type'].value_counts()

df[['year','month','declaration_type']].groupby(['year','month']).describe()

m=df[['year','declaration_type']]
plt.pyplot.figure(figsize=(8,5))
sns.boxplot(x='declaration_type',y='year',data=m)

plt.pyplot.figure(figsize=(8,5))
sns.barplot(x='declaration_type',y='count',data=df['declaration_type'].value_counts().reset_index())

m=df[['year','month','day','declaration_type']].groupby(['year','month','day']).count()
m.reset_index().sort_values(by='declaration_type',ascending=False)

#13/03/20
df.query('year=="{0}" & month=="{1}" & day =="{2}"'.format(2020,3,13))['declaration_title'].value_counts()

m = df.query('year=="{0}" & declaration_title=="Covid-19"'.format(2020))
plt.pyplot.figure(figsize=(20,10))
sns.countplot(x='state',data=m.sort_values(by='time'))

#13/01/1996
df.query('year=="{0}" & month=="{1}" & day =="{2}"'.format(1996,1,13))['declaration_title'].unique()

df.query('year=="{0}" & month=="{1}" & day =="{2}"'.format(2020,4,4))['declaration_title'].unique()

#September 2005
m=df.query('year=="{0}" & month=="{1}"'.format(2005,9))
m['declaration_title'].value_counts()

plt.pyplot.figure(figsize=(16,16))
sns.countplot(x='declaration_title',data=m.sort_values(by='time'),hue='state')

m = df.query('ia_program_declared == "0" & ih_program_declared == "0" & pa_program_declared =="0"')
m['incident_type'].value_counts()

pt = df.pivot_table(values ='disaster_number', index = 'state', columns = 'year').fillna(0)
plt.pyplot.figure(figsize=(12,8))
sns.heatmap(pt, cmap='coolwarm')
plt.pyplot.savefig('heatmap.png')