import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask,render_template,request,redirect
import pickle


app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=['POST']) 
def PredictDisease():

    #int_features=[float(x) for x in  request.form.values()]   
    Temperature =request.form['Temperature']
    Humidity =request.form['Humidity']
    Rainfall =request.form['Rainfall']
    #  final_features=np.array(Temperature,Humidity,)
    prediction=model.predict([[Temperature,Humidity,Rainfall]])
    output=round(prediction[0],2)
    if output <=0:
        result="No"
    else:
        result="Yes"
    return render_template("index.html",prediction_text='Is there disease attack {}'.format(result))


if __name__ == "__main__":
    app.run(debug=True)
    