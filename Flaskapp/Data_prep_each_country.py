import pandas as pd
import matplotlib

dtf_last_confirmed = pd.read_csv("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv")
dtf_last_deaths = pd.read_csv("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv")
dtf_last_recovered = pd.read_csv("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv")

dtf_confirmed = dtf_last_confirmed.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum().T

dtf_deaths = dtf_last_deaths.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum().T

dtf_recovered = dtf_last_recovered.drop(['Province/State','Lat','Long'], axis=1).groupby("Country/Region").sum().T

dtf_active=dtf_confirmed-dtf_deaths-dtf_recovered

dtf_new_cases=dtf_confirmed-dtf_confirmed.shift(1)
dtf_new_cases=dtf_new_cases.fillna(method='bfill')

dtf_confirmed["Date"]=dtf_confirmed.index
dtf_deaths["Date"]=dtf_confirmed.index
dtf_recovered["Date"]=dtf_confirmed.index
dtf_active["Date"]=dtf_confirmed.index
dtf_new_cases["Date"]=dtf_confirmed.index

#dtf_confirmed.to_csv(r'Confirmed.csv', index = False)
#dtf_deaths.to_csv(r'Deaths.csv', index = False)
#dtf_recovered.to_csv(r'Recovered.csv', index = False)
#dtf_active.to_csv(r'Active.csv', index = False)
#dtf_new_cases.to_csv(r'New_cases.csv', index = False)
def get_confirmed():
    return dtf_confirmed
def get_deaths():
    return dtf_deaths
def get_recovered():
    return dtf_recovered
def get_active():
    return dtf_active
def get_newcases():
    return dtf_new_cases
