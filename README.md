## Fraudguard

This repository is dedicated to revolutionizing the security of online transactions by harnessing the power of state-of-the-art machine learning algorithms. With the exponential growth of online transactions, the need for robust fraud detection mechanisms has become paramount. FraudGuard ML combines cutting-edge data analytics techniques with advanced predictive modeling to proactively identify potentially fraudulent credit card transactions, adding an indispensable layer of protection in the constantly evolving landscape of online commerce. By leveraging the vast amounts of transactional data, FraudGuard ML learns intricate patterns and trends, enabling it to effectively flag potential fraud.

Last Updated: 2023-07-05.


---

## *Technologies*

- **Programming Language:** Python
- **Libraries:** Pandas, pathlib, plotly, scikit-learn, numpy, matplotlib,seaborn, imbalanced-learn, pipeline and column transformer, randomizedSearchCV, warninngs, flask, Werkzeug, os, joblib

- **Framework:** JupyterLab
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