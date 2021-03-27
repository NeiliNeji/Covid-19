import json
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly
from DataPreprocessing_Global_Map import get_global_data,get_map_data
from Data_prep_each_country import get_confirmed,get_deaths,get_recovered,get_active,get_newcases

def plot_daywise_line():
    df = get_global_data()
    date = df['Date']
    fig = [go.Line(x=date, y=df['Confirmed'], name='Confirmed'),
           go.Line(x=date, y=df['New Cases'], name='New Cases'),
           go.Line(x=date, y=df['Deaths'], name='Deaths'),
           go.Line(x=date, y=df['Active'], name='Active'),
           go.Line(x=date, y=df['Recovered'], name='Recovered'),
           go.Figure().update_layout(title='Day Wise COVID Spread', xaxis_title="Date", yaxis_title="Data")]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def plot_daywise_bar():
    df = get_global_data()
    date = df['Date']
    fig = [go.Bar(x=date, y=df['Confirmed'], name='Confirmed'),
           go.Bar(x=date, y=df['New Cases'], name='New Cases'),
           go.Bar(x=date, y=df['Deaths'], name='Deaths'),
           go.Bar(x=date, y=df['Active'], name='Active'),
           go.Bar(x=date, y=df['Recovered'], name='Recovered'),
           go.Figure().update_layout(barmode='stack', title='Day Wise COVID Spread')
           ]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def plot_Pie_Chart():
    df = get_global_data()
    labels = ['Confirmed','Deaths','Active','Recovered']
    values = [df['Confirmed'].iloc[-1] , df['Deaths'].iloc[-1], df['Active'].iloc[-1],df['Recovered'].iloc[-1]]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def top_ten_hbar( col, n, hover_data=[]):
    df = get_map_data()
    df = df.sort_values(col).tail(n)
    fig = [go.Bar(x=df[col],
                  y=df['Countries'],
                  hovertext=hover_data,
                  orientation='h',
                  marker_color=df[col]
                  )]
    graphJson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJson

def plot_table():
    df = get_map_data().set_index('Countries')
    df.index = """<a href="Countryinfo/""" + df.index + """ " target="_blank"><div>""" + df.index + '</div></a>'
    df = df.to_html(escape=False)
    return df
def Countryinfoo(name):
    df = get_map_data()
    country=df[df["Countries"]==name]
    return(country)

def plot_confirmed_line(name):
    df = get_confirmed()
    date = df['Date'].astype('datetime64[ns]')
    fig = [go.Line(x=date, y=df[name].values, name='Confirmed'),
           go.Figure().update_layout(title='Day Wise Confirmed Cases', xaxis_title="Date", yaxis_title="Data")]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def plot_deaths_line(name):
    df = get_deaths()
    date = df['Date'].astype('datetime64[ns]')
    fig = [go.Line(x=date, y=df[name].values, name='Deaths'),
           go.Figure().update_layout(title='Day Wise Deaths Cases', xaxis_title="Date", yaxis_title="Data")]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def plot_active_line(name):
    df = get_active()
    date = df['Date'].astype('datetime64[ns]')
    fig = [go.Line(x=date, y=df[name].values, name='Active'),
           go.Figure().update_layout(title='Day Wise Active Cases', xaxis_title="Date", yaxis_title="Data")]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def plot_recovered_line(name):
    df = get_recovered()
    date = df['Date'].astype('datetime64[ns]')
    fig = [go.Line(x=date, y=df[name].values, name='Recovered'),
           go.Figure().update_layout(title='Day Wise Recovered Cases', xaxis_title="Date", yaxis_title="Data")]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def plot_new_cases_line(name):
    df = get_newcases()
    date = df['Date'].astype('datetime64[ns]')
    fig = [go.Line(x=date, y=df[name].values, name='New_cases'),
           go.Figure().update_layout(title='Day Wise New Cases', xaxis_title="Date", yaxis_title="Data")]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def plot_Prediction(arima,polyreg):
    df_arima = pd.read_csv(arima)
    df_polyreg = pd.read_csv(polyreg)

    date = df_arima['Date'].astype('datetime64[ns]')
    fig = [go.Line(x=date[:len(date)-10], y=df_arima["Active"][:len(date)-10], name='Real'),
           go.Line(x=date[len(date)-10:], y=df_arima["Active"][len(date)-10:], name='ARIMA'),
           go.Line(x=date[len(date)-10:], y=df_polyreg["Active"][len(date)-10:], name='Polynomial Regression'),
           go.Figure().update_layout(title='Day Wise Active Prediction', xaxis_title="Date", yaxis_title="Data")]
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
