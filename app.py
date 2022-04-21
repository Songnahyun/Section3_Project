import os
from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict', methods = ['POST'])
def make_prediction():
    data1 = request.form['category']
    data2 = request.form['Age']
    data3 = request.form['type']
    data4 = request.form['gender']
    arr = np.array([[data1, data2, data3, data4]])
    data = model.predict(arr)
    return render_template('after.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)