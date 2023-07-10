## Fraudguard

This repository is dedicated to revolutionizing the security of online transactions by harnessing the power of state-of-the-art machine learning algorithms. With the exponential growth of online transactions, the need for robust fraud detection mechanisms has become paramount. FraudGuard ML combines cutting-edge data analytics techniques with advanced predictive modeling to proactively identify potentially fraudulent credit card transactions, adding an indispensable layer of protection in the constantly evolving landscape of online commerce. By leveraging the vast amounts of transactional data, FraudGuard ML learns intricate patterns and trends, enabling it to effectively flag potential fraud.

Last Updated: 2023-07-05.


---

## *Technologies*

- **Programming Language:** Python
- **Libraries:** Pandas, pathlib, plotly, scikit-learn, numpy, matplotlib,seaborn, imbalanced-learn, pipeline and column transformer, randomizedSearchCV, warninngs, flask, Werkzeug, os, joblib, ks_2sample, resample and xgb.

- **Framework:** JupyterLab, Flask
- **Operating Systems:** Mac OS, Microsoft Windows

---

## *Installation Guide*

If you don't have Python, JupyterLab, or Anaconda installed on your operating system:

-**[Install Python](https://www.python.org/downloads/)**

-**[Install JupyterLab](https://jupyter.org/install)**

-**[Install Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html)**


**1. Conda 'dev' Environment** - To run the main application you will need to create a new enviornment that will be compatible with this application, type and enter the following. You will still use the previous steps' command to activate:

        conda create -n env_name python=3.7 anaconda

Activate conda enviorment by running the following function:

        conda activate env_name 

**2. Other Libraries** - It was mentioned earlier that the other required libraries should already be installed with the Anaconda package. To confirm installation for these libraries, you can either use the 'conda list' command followed by the library name to confirm installation. Or, you can install the libraries which will either install successfully or if already installed, will result in a 'requirement already satisfied' message. Listed below are the commands to install each library if needed:
        
        pip install sklearn
        pip install Flask
        pip install Werkzeug
        pip install plotly
        pip install xgboost



**3. Clone Repo**

After completing all prerequisite installations, you're ready to clone this repository to your local machine. To do this, begin by copying the SSH keys.

Next, navigate to the directory in your terminal where you want this repository to be placed. Once you're in your desired directory, execute the following command:

        git clone 'paste ssh keys here'

To operate the repository in JupyterLab, navigate into the repository folder by typing:

        cd 'repository folder name'

Then, initiate JupyterLab by entering:

        jupyter lab

Navigate to FraudGuard file 

---

## *Usage*

To use this application, you need to have Python and Flask installed on your machine. Follow the steps below to run the application:

1. **Clone the repository**: Start by cloning this repository to your local machine using the following command:

    ```bash
    git clone <repository-link>
    ```

2. **Navigate to the repository folder**: Change your current directory to the cloned repository's directory:

    ```bash
    cd <repository-name>
    ```

3. **Install the requirements**: Install the required Python packages using the requirements file (if present) with the following command:

    ```bash
    pip install -r requirements.txt
    ```

    Or install Flask, pandas, Werkzeug, and joblib manually using pip:

    ```bash
    pip install flask pandas Werkzeug joblib
    ```

4. **Run the application**: Start the Flask server using the following command:

    ```bash
    python <app-name>.py
    ```

    If your Flask application is in a file called `app.py`, you'd use:

    ```bash
    python app.py
    ```

5. **Use the application**: Open a web browser and navigate to `http://127.0.0.1:5000/`. Here you can upload a .csv file and the application will return predictions based on the models loaded.

Note: Make sure the three model files `log_reg_model.pkl`, `ran_for_model.pkl`, and `svm_clf_model.pkl` are present in the root directory of your application.

## Using VS Code

To use this application, you need to have Python, Flask, and Visual Studio Code installed on your machine. Follow the steps below to run the application:

1. **Clone the repository**: Start by cloning this repository to your local machine using the following command:

    ```bash
    git clone <repository-link>
    ```

2. **Navigate to the repository folder**: Change your current directory to the cloned repository's directory:

    ```bash
    cd <repository-name>
    ```

3. **Open the repository in VS Code**: To open the repository folder in VS Code, use the following command:

    ```bash
    code .
    ```

4. **Install the requirements**: Install the required Python packages using the requirements file (if present) with the following command:

    ```bash
    pip install -r requirements.txt
    ```

    Or install Flask, pandas, Werkzeug, and joblib manually using pip:

    ```bash
    pip install flask pandas Werkzeug joblib
    ```

5. **Run the application**: In VS Code, you can run the application by pressing `F5` (ensure you have the Python extension installed). Alternatively, you can use the terminal in VS Code and type:

    ```bash
    python <app-name>.py
    ```

    If your Flask application is in a file called `app.py`, you'd use:

    ```bash
    python app.py
    ```

6. **Use the application**: Open a web browser and navigate to `http://127.0.0.1:5000/`. Here you can upload a .csv file and the application will return predictions based on the models loaded.

Note: Make sure the three model files `log_reg_model.pkl`, `ran_for_model.pkl`, and `svm_clf_model.pkl` are present in the root directory of your application.


---

## *References*
- [plotly Usage](https://plotly.com/python/)
- [flask Usage](https://pypi.org/project/Flask/)
- [scikit-learn](https://www.analyticsvidhya.com/blog/2015/01/scikit-learn-python-machine-learning-tool/)
- [werkzeug usage](https://pypi.org/project/Werkzeug/)
---

## *Summary*

The analysis conducted on the credit card transaction fraud dataset yielded the following results:

1. Data Preprocessing:
   - Duplicates Removal: Duplicate rows were removed from the dataset to ensure data integrity.
   - Column Removal: The 'Time' column was dropped as it was not considered relevant for the analysis.
   - Null Values Check: No null values were found in the dataset.
   - Outlier Removal: Outliers in the 'Amount' column were identified and removed using the IQR method.
   - Standardization: The 'Amount' column was standardized using the StandardScaler.

2. Feature Selection and Engineering:
   - Data Split: The dataset was split into training and testing sets.
   - Class Distribution: The class distribution of fraudulent and non-fraudulent transactions was calculated and visualized.

3. Model Building and Evaluation:
   - Logistic Regression: A logistic regression model was built and evaluated. The model achieved high accuracy, precision, and recall on the training data. On the testing data, it performed well with high accuracy, precision, and recall scores.

   - Random Forest Classifier: A random forest classifier model was built and evaluated. The model demonstrated excellent performance on both the training and testing data, achieving high accuracy, precision, and recall scores.

   - Support Vector Machine (SVM) Classifier: An SVM classifier model was built and evaluated. The SVM model performed well on both the training and testing data, achieving high accuracy, precision, and recall scores.

4. XGBoost Classifier:
   - Confusion Matrix for Testing Predictions:
     ```
     [[31778     6]
      [    8    35]]
     ```
   - Accuracy of the XGBoost Classifier on the Test Dataset: 0.999560121909071
   - Classification Report for the Testing Predictions:
     ```
              precision    recall  f1-score   support

           0       1.00      1.00      1.00     31784
           1       0.85      0.81      0.83        43

     ```
          accuracy                               1.00     31827
          macro avg          0.93      0.91      0.92     31827
          weighted avg       1.00      1.00      1.00     31827
     ```

5. KS Test:
   - KS Statistic: 0.32856289127974003
   - p-value: 5.296912427603326e-28

Overall, the analysis showed that all models, including logistic regression, random forest classifier, SVM classifier, and XGBoost classifier, demonstrated high accuracy, precision, and recall in predicting fraudulent transactions. The XGBoost classifier achieved an accuracy of 0.99956 and performed well in distinguishing between fraudulent and non-fraudulent transactions. The KS test indicated a significant difference in the distribution of the 'Amount' feature between fraudulent and non-fraudulent transactions. These results suggest that the developed models and the identified feature can be useful in detecting and preventing credit card fraud.

---
## *Contributors*

**Rosalinda Olvera Fernandez**

[GitHub](https://github.com/rolvera05) - rolvera98271@gmail.com

**Alex Valenzuela**

[GitHub](axvalenzuela@gmail.com) - axvalenzuela@gmail.com

**James White**

[GitHub](jswhite1992@gmail.com) - jswhite1992@gmail.com

**Michelle Silver**

[GitHub](supersilver1978@gmail.com) - supersilver1978@gmail.com

**Dylan Johnston**

[GitHub](dylanhjjohnston@gmail.com) - dylanhjjohnston@gmail.com

---
