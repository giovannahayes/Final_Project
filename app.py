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