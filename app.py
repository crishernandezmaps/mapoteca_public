from flask import Flask, render_template, request, session, redirect, url_for
import os
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():   
    return render_template('index.html')

@app.route('/fscl', methods=['GET', 'POST'])
def fscl():
    city = 'santiago'
    data = f'data/{city}.csv'
    df = pd.read_csv(data, index_col=False)
    if request.method == 'POST':
        category = request.form['selector'].lower()
        print(category)    
        m = df[[category, 'lat', 'lon']]
        m.sort_values(by=[category], ascending=False, inplace=True)
        to_map = m.loc[m[category] >= 0.8]
        print(df.shape, m.shape, to_map.shape)
        return render_template('index.html')
    return render_template('fscl.html')    

@app.route('/flim', methods=['GET', 'POST'])
def flim():
    city = 'lima'
    data = f'data/{city}.csv'
    df = pd.read_csv(data, index_col=False)
    if request.method == 'POST':
        category = request.form['selector'].lower()
        print(category)    
        m = df[[category, 'lat', 'lon']]
        m.sort_values(by=[category], ascending=False, inplace=True)
        to_map = m.loc[m[category] >= 0.8]
        print(df.shape, m.shape, to_map.shape)
        return render_template('index.html')
    return render_template('flim.html') 

@app.route('/fbog', methods=['GET', 'POST'])
def fbog():
    city = 'bogota'
    data = f'data/{city}.csv'
    df = pd.read_csv(data, index_col=False)
    if request.method == 'POST':
        category = request.form['selector'].lower()
        print(category)    
        m = df[[category, 'lat', 'lon']]
        m.sort_values(by=[category], ascending=False, inplace=True)
        to_map = m.loc[m[category] >= 0.8]
        print(df.shape, m.shape, to_map.shape)
        return render_template('index.html')
    return render_template('fbog.html')   

@app.route('/fmex', methods=['GET', 'POST'])
def fmex():
    city = 'mexico'
    data = f'data/{city}.csv'
    df = pd.read_csv(data, index_col=False)
    if request.method == 'POST':
        category = request.form['selector'].lower()
        print(category)    
        m = df[[category, 'lat', 'lon']]
        m.sort_values(by=[category], ascending=False, inplace=True)
        to_map = m.loc[m[category] >= 0.8]
        print(df.shape, m.shape, to_map.shape)
        return render_template('index.html')
    return render_template('fmex.html')    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))