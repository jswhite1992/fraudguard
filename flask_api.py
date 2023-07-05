from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pandas as pd
import os
import joblib

# Initialize Flask application
app = Flask(__name__)

# If upload directory does not exist, create it
if not os.path.exists('static/uploads'):
    os.makedirs('static/uploads')

# Folder to upload files
UPLOAD_FOLDER = './static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load models globally (at application startup)
log_reg = joblib.load("log_reg_model.pkl")
ran_for = joblib.load("ran_for_model.pkl")
svm_clf = joblib.load("svm_clf_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if a file is selected
        if 'file' not in request.files:
            return "No file uploaded."

        # Get the file
        file = request.files['file']

        # If the user does not select a file, browser submits an empty file without a filename
        if file.filename == '':
            return "No selected file."

        # Save the uploaded file
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Load the dataset
            data = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Perform predictions using pre-loaded models
        lr_prediction = log_reg.predict(data)
        rf_prediction = ran_for.predict(data)
        svm_prediction = svm_clf.predict(data)

        # Count the number of fraudulent and non-fraudulent transactions
        lr_fraud = sum(lr_prediction)
        rf_fraud = sum(rf_prediction)
        svm_fraud = sum(svm_prediction)

        lr_non_fraud = len(lr_prediction) - lr_fraud
        rf_non_fraud = len(rf_prediction) - rf_fraud
        svm_non_fraud = len(svm_prediction) - svm_fraud

        return render_template('result.html', lr_fraud=lr_fraud, rf_fraud=rf_fraud, svm_fraud=svm_fraud, lr_non_fraud=lr_non_fraud, rf_non_fraud=rf_non_fraud, svm_non_fraud=svm_non_fraud)

if __name__ == "__main__":
    app.run(debug=True)