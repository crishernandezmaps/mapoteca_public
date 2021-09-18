from flask import Flask, render_template, request, session, redirect, url_for
import os
import pandas as pd
import json
from keplergl import KeplerGl

# FOR THE MAP
conf_scl = json.load(open('data/config_santiago.json',))
conf_lim = json.load(open('data/config_lima.json',))
conf_bog = json.load(open('data/config_bogota.json',))
conf_mex = json.load(open('data/config_mexico.json',))

txt_html = b'''<meta charset="utf-8">
            <title>Mapoteca</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <meta name="description" content="Mapoteca Public">
            <meta name="keywords" content="Mapoteca, Maps, Geospatial, Insights, Mobility">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/simple-line-icons/2.4.1/css/simple-line-icons.css" />
            <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@200&display=swap" rel="stylesheet" />            
            <style>
                @import url('https://fonts.googleapis.com/css?family=Montserrat:600&display=swap');
                div.nav-inside {
                    position: absolute;
                    z-index: 30;
                    top: -1%;
                    right: 3%;
                    margin-bottom: 5%;
                }
                div.nav-inside > ul > li  {
                    display: inline-block;
                    zoom: 1;
                    display: inline;
                }
                div.nav-inside > ul > li > a {
                    color: rgb(255, 255, 255);
                    font-size: 20px;
                    line-height: 1.71429;
                    font-weight: 400;
                    font-size: 0.8em;
                    text-decoration: none;
                }
                .map-control {
                    margin-top: 150px !important;
                }
                .geocoder-panel {
                    top: 166px !important;
                    right: 60px !important;
                }
                button {
                    margin: 50px;
                    font-family: inherit;
                }                
                .fill {
                    z-index: 100; 
                    position: absolute;
                    right: 0%;
                    font-size: 20px;
                    font-weight: 200;
                    font-family: 'Montserrat', sans-serif;
                    letter-spacing: 1px;
                    padding: 13px 50px 13px;
                    outline: 0;
                    border: 1px solid #0DFF92;
                    cursor: pointer;
                    background-color: rgba(0, 0, 0, 0);
                }

                .fill::after {
                    content: "";
                    background-color: #0DFF92;
                    width: 100%;
                    z-index: -1;
                    position: absolute;
                    height: 100%;
                    top: 7px;
                    left: 7px;
                    transition: 0.2s;
                }

                .fill:hover::after {
                    top: 0px;
                    left: 0px;
                }                
            </style>
            <a href="./"><button type="button" class="fill">Volver</button></a>'''

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
        map_1 = KeplerGl(config=conf_scl, data={'data': m}, options={"readOnly": True, "centerMap": True})
        r = txt_html + map_1._repr_html_()
        return r        
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
        map_1 = KeplerGl(data={'data': m}, config=conf_lim, options={"readOnly": True, "centerMap": True})
        r = txt_html + map_1._repr_html_()
        return r        
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
        map_1 = KeplerGl(data={'data': m}, config=conf_bog, options={"readOnly": True, "centerMap": True})
        r = txt_html + map_1._repr_html_()
        return r  
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
        map_1 = KeplerGl(data={'data': m}, config=conf_mex, options={"readOnly": True, "centerMap": True})
        r = txt_html + map_1._repr_html_()
        return r
    return render_template('fmex.html')    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))