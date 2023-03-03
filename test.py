## Python test file for flask to test locally
import requests as r
import pandas as pd
import json


base_url = 'http://127.0.0.1:5000/' #base url local host

json_data = [
    {
    "ApplicantIncome" : 3541,
    "CoapplicantIncome" : 0.0,
    "LoanAmount" : 112.0,
    "Loan_Amount_Term" : 360.0,
    "Total_Income_Log" : 11.0,
    "Female" : 1.0,
    "Male" : 0.0,
    "No" : 1.0,
    "Yes" : 0.0,
    "Not Married" : 1.0,
    "Graduate" : 1.0,
    "Not Graduate": 0.0,
    "0.0":1.0,
    "1.0":0.0,
    "Rural":0.0,
    "Semiurban":1.0,
    "Urban":0.0,
    "0":0.0,
    "1":0.0,
    "2":1.0,
    "3+":0.0,
    }
]



# Get Response
# response = r.get(base_url)
response = r.post(base_url + "predict", json = json_data)


if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')
