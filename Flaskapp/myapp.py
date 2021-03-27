from flask import Flask, render_template, request, \
    session, redirect, url_for, flash

from mymodels import plot_daywise_bar, plot_daywise_line,plot_Pie_Chart,top_ten_hbar,plot_table,Countryinfoo,\
                     plot_confirmed_line,plot_deaths_line,plot_active_line, \
                     plot_recovered_line,plot_new_cases_line,plot_Prediction
from testmap import map_active_percent,map_active
from bokeh.embed import components

app = Flask(__name__, static_url_path='/assets',
            static_folder='./covidtrack/assets',
            template_folder='./templates')




@app.route('/')
@app.route('/myindex.html')
def root():
    return render_template('myindex.html')


@app.route('/stats.html')
def stats():

    bar = plot_daywise_bar()
    line = plot_daywise_line()
    pie = plot_Pie_Chart()
    topTenCases = top_ten_hbar( 'Confirmed', 10)
    topTenDeaths = top_ten_hbar( 'Deaths', 10)
    topTenRecovered = top_ten_hbar( 'Recovered', 10)
    topTenActive = top_ten_hbar( 'Active', 10)
    table=plot_table()

    return render_template('stats.html', plot=bar, line=line,pie=pie,topTenCases=topTenCases,
                           topTenDeaths=topTenDeaths,topTenRecovered=topTenRecovered,
                           topTenActive=topTenActive,table=table)
#<div style="width: 20%; display: inline-block;">
#{{ div | safe }}
#{{ script | safe }}
#</div>

@app.route('/myworldmap.html')
def worldmap():
    active_percent=map_active_percent()
    active=map_active()
    script_active_percent, div_active_percent = components(active_percent)
    script_active, div_active = components(active)

    return render_template('myworldmap.html',script_active_percent = script_active_percent,
                           div_active_percent = div_active_percent,script_active=script_active,
                           div_active=div_active)

@app.route('/Countryinfo/<name>')
def Countryinfo(name):
    info=Countryinfoo(name)
    Active=str(info["Active"].values).strip('[]')
    Confirmed=str(info["Confirmed"].values).strip('[]')
    Deaths=str(info["Deaths"].values).strip('[]')
    Recovered=str(info["Recovered"].values).strip('[]')
    confirmed_line=plot_confirmed_line(name)
    active_line=plot_active_line(name)
    deaths_line=plot_deaths_line(name)
    recovered_line=plot_recovered_line(name)
    new_cases_line=plot_new_cases_line(name)
    
    return render_template('Country.html', name=name,confirmed_line=confirmed_line,active_line=active_line,
                           deaths_line=deaths_line,recovered_line=recovered_line,new_cases_line=new_cases_line,
                           Active=Active,Confirmed=Confirmed,Deaths=Deaths,Recovered=Recovered)

@app.route('/prediction.html')
def prediction():

    Global_Prediction = plot_Prediction("Global_Prediction_Arima.csv","Global_Prediction_PolyReg.csv")
    Tunisia_Prediction = plot_Prediction("Tunisia_Prediction_Arima.csv","Tunisia_Prediction_PolyReg.csv")

   


    return render_template('prediction.html',Global_Prediction=Global_Prediction,Tunisia_Prediction=Tunisia_Prediction)

if __name__ == '__main__':
    app.run(debug=True)
