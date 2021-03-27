import pandas as pd
import matplotlib

dtf_last_confirmed = pd.read_csv("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv")
dtf_last_deaths = pd.read_csv("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv")
dtf_last_recovered = pd.read_csv("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv")

dtf_confirmed = dtf_last_confirmed.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum().T

dtf_deaths = dtf_last_deaths.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum().T

dtf_recovered = dtf_last_recovered.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum().T


X=dtf_confirmed.sum(axis=1)
Y=dtf_recovered.sum(axis=1)
Z=dtf_deaths.sum(axis=1)
A=X-(Y+Z)
df = pd.DataFrame (columns = ['Date','New Cases','Active','Confirmed','Deaths','Recovered'])

df['Date']=X.index
df['Date'] = df['Date'].astype('datetime64[ns]')


df['Confirmed']=X.values
df["New Cases"] = df["Confirmed"] - df["Confirmed"].shift(1)
df["New Cases"] = df["New Cases"].fillna(method='bfill')
df["New Cases"] = df["New Cases"].astype(int)
df["Active"]=A.values
df["Deaths"]=Z.values
df["Recovered"]=Y.values
#df.to_csv(r'Global_Data.csv', index = False)

dtf_confirmed = dtf_last_confirmed.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum()

dtf_deaths = dtf_last_deaths.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum()

dtf_recovered = dtf_last_recovered.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum()

dtf_active=dtf_confirmed-dtf_deaths-dtf_recovered

population=pd.read_csv("population.csv")
newpop=population[['Country (or dependency)','Population (2020)']]
newpop.replace('South Korea', 'Korea, South', inplace = True)
newpop.replace('DR Congo', 'Congo (Kinshasa)', inplace = True)
newpop.replace('Congo', 'Congo (Brazzaville)', inplace = True)
newpop.replace('Czech Republic (Czechia)', 'Czechia', inplace = True)
newpop.replace('Saint Kitts & Nevis', 'Saint Kitts and Nevis', inplace = True)
newpop.replace('St. Vincent & Grenadines', 'Saint Vincent and the Grenadines', inplace = True)
newpop.replace('Sao Tome & Principe', 'Sao Tome and Principe', inplace = True)
newpop.replace('Taiwan', 'Taiwan*', inplace = True)
newpop.replace('United States', 'US', inplace = True)
newpop.replace('State of Palestine', 'West Bank and Gaza', inplace = True)
newpop.replace("Côte d'Ivoire", "Cote d'Ivoire", inplace = True)
newpop.replace('Myanmar', 'Burma', inplace = True)

dtf_confirmed=dtf_confirmed.iloc[:,-1]
dtf_deaths=dtf_deaths.iloc[:,-1]
dtf_recovered=dtf_recovered.iloc[:,-1]
dtf_active=dtf_active.iloc[:,-1]

df1 = pd.DataFrame (columns = ['Countries','Active','Confirmed','Deaths','Recovered'])
df1['Countries']=dtf_confirmed.index
df1['Active']=dtf_active.values
df1['Confirmed']=dtf_confirmed.values
df1['Deaths']=dtf_deaths.values
df1['Recovered']=dtf_recovered.values
df_outer = pd.merge(df1, newpop, left_on='Countries', right_on='Country (or dependency)')
df_outer['Active Percent']= (df_outer['Active']/df_outer['Population (2020)'])*100
df_outer = df_outer.drop("Country (or dependency)", axis=1)

#df_outer.to_csv(r'Map_Data.csv', index = False)

def get_global_data():
    return df
def get_map_data():
    return df_outer




