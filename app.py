import numpy as np
import pickle
from flask import Flask, request, render_template

# Create app
app = Flask(__name__)

# Use pickle to load in the pre-trained model.
 
with open(f'rf.sav', 'rb')as f: 
    model = pickle.load(f)

    # with open(f'LogisticOverSample.sav', "rb") as f:
    # model = pickle.load(f)

# with open(f'model/rfmodel.pkl', 'rb')


# as f:
#     model = pickle.load(f)
# Bind home function to URL


@app.route("/")
def home():
    return render_template("index.html")


# Bind predict function to URL
@app.route("/predict", methods=["Get","POST"])
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
                               result="You are approved")
    else:
        return render_template("index.html",
                               result="You are denined")


# app = flask.Flask(__name__, template_folder='templates')

# with open(f'model/rfmodel.pickle', 'rb') as f:
#     model = pickle.load(f)


# @app.route("/", methods=['GET', 'POST'])
# def main():

#     if flask.request.method == 'Get':
#         return( flask.render_template('index.html'))

    return(render_template("index.html"))


if __name__ == '__main__':
    app.run()