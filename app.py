from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
app.debug = True

@app.route('/')
def home():
    #Get values from api
    currency_from = request.args.get('currency_from')
    currency_to = request.args.get('currency_to')
    amount = request.args.get('amount')

    #Get request from api
    url = f'https://api.exchangerate.host/convert?from={currency_from}&to={currency_to}&amount={amount}'
    response = requests.get(url)
    data = response.json()
    print(data)



    return render_template('index.html')