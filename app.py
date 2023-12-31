import requests
from currency_symbols import CurrencySymbols
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)
app.debug = True


@app.route("/")
def home():
    # Get values from api
    currency_from = request.args.get("from")
    currency_to = request.args.get("to")
    amount = request.args.get("amount")
    currencies_list = {
        "ALL": "Albania Lek",
        "AFN": "Afghanistan Afghani",
        "ARS": "Argentina Peso",
        "AWG": "Aruba Guilder",
        "AUD": "Australia Dollar",
        "AZN": "Azerbaijan New Manat",
        "BSD": "Bahamas Dollar",
        "BBD": "Barbados Dollar",
        "BDT": "Bangladeshi taka",
        "BYR": "Belarus Ruble",
        "BZD": "Belize Dollar",
        "BMD": "Bermuda Dollar",
        "BOB": "Bolivia Boliviano",
        "BAM": "Bosnia and Herzegovina Convertible Marka",
        "BWP": "Botswana Pula",
        "BGN": "Bulgaria Lev",
        "BRL": "Brazil Real",
        "BND": "Brunei Darussalam Dollar",
        "KHR": "Cambodia Riel",
        "CAD": "Canada Dollar",
        "KYD": "Cayman Islands Dollar",
        "CLP": "Chile Peso",
        "CNY": "China Yuan Renminbi",
        "COP": "Colombia Peso",
        "CRC": "Costa Rica Colon",
        "HRK": "Croatia Kuna",
        "CUP": "Cuba Peso",
        "CZK": "Czech Republic Koruna",
        "DKK": "Denmark Krone",
        "DOP": "Dominican Republic Peso",
        "XCD": "East Caribbean Dollar",
        "EGP": "Egypt Pound",
        "SVC": "El Salvador Colon",
        "EEK": "Estonia Kroon",
        "EUR": "Euro Member Countries",
        "FKP": "Falkland Islands (Malvinas) Pound",
        "FJD": "Fiji Dollar",
        "GHC": "Ghana Cedis",
        "GIP": "Gibraltar Pound",
        "GTQ": "Guatemala Quetzal",
        "GGP": "Guernsey Pound",
        "GYD": "Guyana Dollar",
        "HNL": "Honduras Lempira",
        "HKD": "Hong Kong Dollar",
        "HUF": "Hungary Forint",
        "ISK": "Iceland Krona",
        "INR": "India Rupee",
        "IDR": "Indonesia Rupiah",
        "IRR": "Iran Rial",
        "IMP": "Isle of Man Pound",
        "ILS": "Israel Shekel",
        "JMD": "Jamaica Dollar",
        "JPY": "Japan Yen",
        "JEP": "Jersey Pound",
        "KZT": "Kazakhstan Tenge",
        "KPW": "Korea (North) Won",
        "KRW": "Korea (South) Won",
        "KGS": "Kyrgyzstan Som",
        "LAK": "Laos Kip",
        "LVL": "Latvia Lat",
        "LBP": "Lebanon Pound",
        "LRD": "Liberia Dollar",
        "LTL": "Lithuania Litas",
        "MKD": "Macedonia Denar",
        "MYR": "Malaysia Ringgit",
        "MUR": "Mauritius Rupee",
        "MXN": "Mexico Peso",
        "MNT": "Mongolia Tughrik",
        "MZN": "Mozambique Metical",
        "NAD": "Namibia Dollar",
        "NPR": "Nepal Rupee",
        "ANG": "Netherlands Antilles Guilder",
        "NZD": "New Zealand Dollar",
        "NIO": "Nicaragua Cordoba",
        "NGN": "Nigeria Naira",
        "NOK": "Norway Krone",
        "OMR": "Oman Rial",
        "PKR": "Pakistan Rupee",
        "PAB": "Panama Balboa",
        "PYG": "Paraguay Guarani",
        "PEN": "Peru Nuevo Sol",
        "PHP": "Philippines Peso",
        "PLN": "Poland Zloty",
        "QAR": "Qatar Riyal",
        "RON": "Romania New Leu",
        "RUB": "Russia Ruble",
        "SHP": "Saint Helena Pound",
        "SAR": "Saudi Arabia Riyal",
        "RSD": "Serbia Dinar",
        "SCR": "Seychelles Rupee",
        "SGD": "Singapore Dollar",
        "SBD": "Solomon Islands Dollar",
        "SOS": "Somalia Shilling",
        "ZAR": "South Africa Rand",
        "LKR": "Sri Lanka Rupee",
        "SEK": "Sweden Krona",
        "CHF": "Switzerland Franc",
        "SRD": "Suriname Dollar",
        "SYP": "Syria Pound",
        "TWD": "Taiwan New Dollar",
        "THB": "Thailand Baht",
        "TTD": "Trinidad and Tobago Dollar",
        "TRY": "Turkey Lira",
        "TRL": "Turkey Lira",
        "TVD": "Tuvalu Dollar",
        "UAH": "Ukraine Hryvna",
        "GBP": "United Kingdom Pound",
        "USD": "United States Dollar",
        "UYU": "Uruguay Peso",
        "UZS": "Uzbekistan Som",
        "VEF": "Venezuela Bolivar",
        "VND": "Viet Nam Dong",
        "YER": "Yemen Rial",
        "ZWD": "Zimbabwe Dollar",
    }

    # Get request from api/Turn into JSON to retrieve data from a JSON Dictionary
    url = f"https://api.exchangerate.host/convert?from={currency_from}&to={currency_to}&amount={amount}"
    response = requests.get(url)
    data = response.json()

    #Grab currency symbol corresponded to the currency we want to convert to 
    currency_symbol = CurrencySymbols.get_symbol(data["query"]["to"])

    #Converted amount
    result = data["result"]

    # Validation Checks
    error_message = None
    #Check to see if the currency from/to are filled in
    if not currency_from or not currency_to:
        error_message = "Please provide two currencies"
    #Check to see if the currencies are valid
    elif currency_from not in currencies_list or currency_to not in currencies_list:
        error_message = "Please provide a valid currency"
    #Check to see if amount is filled in and is a number
    elif not amount or not amount.isdigit():
        error_message = "Please provide a valid amount"
    # If there is a incorrect input...
    if error_message:
        return render_template("index.html", error_message=error_message)

    return render_template(
        "index.html", result="%.2f" % result, currency=currency_symbol
    )
