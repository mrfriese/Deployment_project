from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd


# App definition
app = Flask(__name__)

# importing models
with open('notebooks/pickled_bank.pkl', 'rb') as f:
   regressor = pickle.load (f)

@app.route('/')
def welcome():
   return "Welcome!"

@app.route('/predict', methods=['POST','GET'])
def predict():
   

   if flask.request.method == 'GET':
       return "Prediction page. This page will check some banking information to see if you are eligable for a loan."

   if flask.request.method == 'POST':
       try:
           json = request.json # '' since 'json' is a special word
           print(json)
           query_ = pd.DataFrame(json)
           # query_ = pd.getdummies(pd.DataFrame(json))
           query = query_.reindex(fill_value= 0)
           prediction = list(regressor.predict(query))

           return jsonify({
               "prediction":str(prediction)
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })



if __name__ == "__main__":
   app.run()

