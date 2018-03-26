from flask import Flask, render_template, request, redirect
import requests
import numpy as np
import pandas as pd
from bokeh.plotting import figure as bokehfigure
from bokeh.embed import components


app = Flask(__name__)

# Create the main plot
#def create_figure(close_data,ticker_symbol):
   # p1 = bokehfigure()
   # p1.grid.grid_line_alpha = 0.3
   # p1.xaxis.axis_label = 'Days'
   # p1.yaxis.axis_label = 'Price'
   # p1.line(range(30),close_data,color = '#A6CEE3',legend = ticker_symbol)
   # return p1

# index page
@app.route('/',methods = ['GET','POST'])   
@app.route('/index',methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        ticker_symbol = request.form['ticker']
        return render_template('figure.html')
        #return render_template('figure.html')
        #ticker_feature = request.form['features']
        #stock_data = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/%s.json?api_key=Y4tZ_xJ8saiyQVoUEQEP'%ticker_symbol)
        #stock_data_dict = stock_data.json()
        #column_names = stock_data_dict['dataset']['column_names']
        #stock_df = pd.DataFrame(stock_data_dict['dataset']['data'],columns = column_names)
        #stock_lm = stock_df[stock_df.last_valid_index() - 29:]
        #close_data = stock_lm.Close
        #p1 = bokehfigure()
        #p1.grid.grid_line_alpha = 0.3
        #p1.xaxis.axis_label = 'Days'
        #p1.yaxis.axis_label = 'Price'
        #xdata = range(1,31,1)
        #p1.line(xdata,close_data,color = '#A6CEE3',legend = ticker_symbol)
        #script,div = components(p1)
        #return render_template('index.html',script = script, div = div)
    #stock_data_dict = stock_data.json()
    #dates = stock_data_dict['dataset']['data'][::13]
    #closing_data = stock_data_dict['dataset']['data'][::3]


if __name__ == '__main__':
  app.run(port=33507)
