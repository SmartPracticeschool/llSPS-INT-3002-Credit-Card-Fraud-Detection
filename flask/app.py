# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 01:42:51 2020

@author: Anindita mishra
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('random.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0]
    if(output==1):
        pred="Fraud"
    else:
        pred="Valid"
    return render_template('index.html', prediction_text='Transaction is {}'.format(pred))
if __name__ == "__main__":
    app.run(debug=True)

