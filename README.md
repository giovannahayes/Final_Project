# Loan Approval Prediction:
## Machine Learning Data Analytics Project

![ML](https://github.com/giovannahayes/Final_Project/blob/main/static/images/mlgif.gif)


## Team members: Alicia Smith, Pooja Patel, Giovanna Hayes

## Link: https://immense-inlet-93772.herokuapp.com/


# Data:
Fictitious Dream Housing Finance company deals in all kinds of home loans. They have presence across all urban, semi urban and rural areas. Customer first applies for home loan and after that company validates the customer eligibility for loan.

The company wants to automate the loan eligibility process (real time) based on customer detail provided while filling online application form. These details are Gender, Marital Status, Education, Number of Dependents, Income, Loan Amount, Credit History and others. To automate this process, they have provided a dataset to identify the customers segments that are eligible for loan amount so that they can specifically target these customers. 

# Goal:
The goal of this project is to use Dream Housing Finance’s loan performance data to make predictions about a given customer. We want to forecast the probability a borrower will be eligible for the loan he/she is applying for


 # Analysis:  
The focus of this analysis is to develop a loan level model that predicts whether a borrower will be eligible to be approved on their loan based on origination and performance information available through Dream House Finance Company.  

Model fitting began with an SVM model on a random sample of the data.  The resulting model had an accuracy score off 78%.  

Running a random forest model on a random sample of data provided better results. The accuracy number was lower 76% but this model allowed for multiple classifications to be layerd into the model. This is an advantage when comparing the random forest model to the SVM model. 

Finally, a deep learning neural network was fitted to the oversampled data set. What we found was that we did not have nearly enough data points in our dataset to leverage this machine learning model to its fullest potential. Using the model resulted in inaccurate predictions and netted an accuracy score of 67%.  


All fitted models seem to be most influenced by income of the loan application. A loan applicant with a higher income, or applicant income combined co-applicant income, had a likelihood of eligibility increasing. 
 
# Conclusion:
Though several modeling techniques were investigated, the best models to provide a prediction of default was the random forest model. This model used is to provide a user with a prediction of eligibility given information enter for an individual loan.


-----------------------------------------------

# Data Management / Cleaning / Flask Coding

1. The Fictitious Dream House Finance data set was downloaded as CSV files from Kaggle.


2. The data was cleaned using Python Pandas. We removed null values and identified outliers. We used sklearn one hot encoder to convert our categorical data to numeric in preparation to fit and train our models.



# Python Flask coding: 
Created the framework of the app.py and template/index.html to build upon.

-----------------------------------------------

# Heroku | www.heroku.com 

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

-----------------------------------------------

# TECHNOLOGY UTILIZED:

### Prerequisites

```
python-3.6.2
Flask==1.1.1
gunicorn==20.0.4
matplotlib==3.1.3
pandas==1.0.1
pickle-mixin==1.0.2
scikit-image==0.16.2
scikit-learn==0.22.1
scipy==1.4.1
seaborn==0.10.0
numpy==1.19.5
HTML5
CSS3


