import numpy as np
import pickle
from flask import Flask, request, render_template
# Create app
app = Flask(__name__, template_folder='Templates')
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
@app.route("/ourstory", methods=["Get","POST"])
def project():
    return render_template("ourstory.html")
@app.route("/data")
def data():
    return render_template("data.html")
@app.route("/visualizations")
def visualizations():
    return render_template("comparison.html")
@app.route("/models")
def models():
    return render_template("mlindex.html")
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
    return(render_template("index.html"))
if __name__ == '__main__':
    app.run()
