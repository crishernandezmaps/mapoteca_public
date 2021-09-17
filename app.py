from flask import Flask, render_template, request, session, redirect, url_for, Blueprint, send_file
import os
from welokat_near import welokat_near

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form['address']
        bot = welokat_near(address)
        data = bot.wnear()  
        print(data)  
        if type(data) == str:    
            return render_template('sorry.html', data=data)
        if type(data) == dict:
            return render_template('result.html', data=data['data'], latlon=data['latlon'], res=data['res'])
        else:
            pass
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

"""
TODO:
- Sorry page
- Check maximun requests by minute
- Limit use by IP
""" 