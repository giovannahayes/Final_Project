<<<<<<< HEAD
import numpy as np
import pickle
from flask import Flask, request, render_template

#Create app
app= Flask(__name__)

# Use pickle to load in the pre-trained model.
with open(f'model/rfmodel.pickle', 'rb') as f:
    model = pickle.load(f)


# Bind home function to URL
@app.route("/")
def home():
    return render_template("index.html")


# Bind predict function to URL
@app.route("/predict", methods =["POST"])
def predict():
 
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
 
    output = prediction
 
    # Check the output values and retrieve the result with html tag based on the value
    if output == 1:
        return render_template("index.html", 
    result = "You are approved")
    else:
        return render_template("index.html", 
    result = "You are denined")


# app = flask.Flask(__name__, template_folder='templates')

# with open(f'model/rfmodel.pickle', 'rb') as f:
#     model = pickle.load(f)


# @app.route("/", methods=['GET', 'POST'])
# def main():

#     if flask.request.method == 'Get':
#         return( flask.render_template('index.html'))

   

    return(flask.render_template("index.html"))
if __name__ == '__main__':
    app.run()


=======
import os

import pandas as pd
import numpy as np
from scipy import stats

from flask import Flask, jsonify, render_template,redirect, request
#from flask_sqlalchemy import SQLAlchemy
from sklearn import model_selection
import pickle
#from sklearn.linear_model import LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)                                                                                                               


#route where html housing dashboard will live
@app.route('/api/v1.0/Dashboard')
def showDashboard():
    return render_template('index_goh.html')
if __name__ == "__main__":
    app.debug = True
    app.run()


# with open(f'finalized_model.sav', "rb") as f:
#     model = pickle.load(f)
# #with open(f'logistic_regression_scaler.pickle', "rb") as f2:
#     #scaler = pickle.load(f2)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     """Return the homepage."""
#     output_message = ""
#     # loaded_model = pickle.load(open('LogisticOverSample.sav', 'rb'))
#     print(model)
#     if request.method == "POST":
#         OriginalGender = (request.form["gender"])
#         # OriginalUPB = (request.form["OriginalUPB"])
#         # OriginalLoanTerm = (request.form["OriginalLoanTerm"])
#         # OriginalLoanToValueLTV = (request.form["OriginalLoanToValueLTV"])
#         # PrimaryMortgageInsurancePercent = (request.form["PrimaryMortgageInsurancePercent"])
#         # OriginalDebtToIncomeRatio = float(request.form["OriginalDebtToIncomeRatio"])
#         # NumberofBorrowers = (request.form["NumberofBorrowers"])
#         # FirstTimeHomeBuyerIndicator = (request.form["FirstTimeHomeBuyerIndicator"])
#         # BorrowerCreditScoreAtOrigination = (request.form["BorrowerCreditScoreAtOrigination"])
#         # CoBorrowerCreditScoreAtOrigination = (request.form["CoBorrowerCreditScoreAtOrigination"])
#         # LoanAge = (request.form["LoanAge"])+
>>>>>>> main
