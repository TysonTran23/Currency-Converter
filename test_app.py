from unittest import TestCase

from app import app
from flask import session
import json

app.config["TESTING"] = True
app.config["DEBUG_TB_HOSTS"] = ["dont-show-debug-toolbar"]


class CurrencyConverterTestCase(TestCase):
    def test_form(self):
        """Test if form is succesfully being submitted"""
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)

    def test_api(self):
        """Test if conversion is getting a correct answer"""
        with app.test_client() as client:
            response = client.get("http://127.0.0.1:5000/?from=USD&to=USD&amount=1")

            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("<h2>The result is $1.00</h2>", html)

    def test_to(self):
        """Test if currency to is left empty, that a error message shows"""
        with app.test_client() as client:
            response = client.get("http://127.0.0.1:5000/?from=USD&to=&amount=100")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("<h2>Please provide two currencies</h2>", html)

    def test_from(self):
        """Test if currency from is left empty, that a error message shows"""
        with app.test_client() as client:
            response = client.get("http://127.0.0.1:5000/?from=&to=USD&amount=100")
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn("<h2>Please provide two currencies</h2>", html)

    def test_amount(self):
        """Test if amount is left empty, that a error message shows"""
        with app.test_client() as client:
            response = client.get("http://127.0.0.1:5000/?from=USD&to=USD&amount=")

            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn("<h2>Please provide a valid amount</h2>", html)

#Ask mentor about this test
# I want this test to check if the currency is in the currency list
# This is how far I got, Can't figure out how to grab the value from the api
# Also wasn't sure if I should use the flask link or the api link
    # def test_currency(self):
    #     """Test if amount is left empty, that a error message shows"""
    #     with app.test_client() as client:
    #         response = client.get("http://127.0.0.1:5000/?from=USD&to=USD&amount=")
    #         response = client.get('https://api.exchangerate.host/convert?from=USD&to=EUR&amount=100')

    #         data = response.json()
    #         value = data['query']['from']
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn(value, app.currency_list)



    
    

        
        
