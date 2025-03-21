# Dover Poly's Repository for BuildingBlocs Hackathon 

This README is split into 2 parts:

1.  Introduction to our solution
2.  Steps to reproduce our solution
    * a) Jupyter Notebook
    * b) Web Application 

## 1. Introduction to our solution

**Hackathon Problem Statement:** "Analyse pertinent data trends concerning the biodiversity sector to improve the sector’s efficiency and abilities."

As the scope of the Hackathon problem statement is massive, we decided to craft our own problem statement (which is a subset of the hackathon's problem statement) so we could work on something that we are more passionate about and see our solution have direct impact.

**Our problem statement:** "How can we protect Endangered Species against Natural Disasters?"
(which is a subset of the hackathon's problem statement)

To tackle this we looked for relevant data online pertaining to these 2 topics and saw that we could analyze the data and glean useful information from historical data. But we wanted to go one step further and try and predict future data of some kind which would allow even more informed strategy and decision making, so that is what we did! :)

## 2. Steps to run the Analysis On Jupyter Notebook

We have 2 parts to our solution:

* a) Analysis and Visualization of data on Endangered Species and Natural Disasters
* b) 2D AI Geospatial Mapping and Simulation for Predictive Analysis of Natural Disasters

Part a) is run on a Jupyter Notebook, whereas part b) is a website that is hosted locally. However, for both, a Python environment is required.

**1. Download the GitHub Repository**
* **In Terminal with Git installed**

    ```
    git clone https://github.com/JovianSanjaya/2D-Mapping-and-Simulation-Approach.git
    ```

**2. (Reccomended) Create and activate Python Virtual Environment**
* **Using venv :**
    ```
    # Install virtualenv (if you don't have it)
    pip install virtualenv

    # Create virtual environment
    python -m venv venv_name

    # Activate virtual environment (Windows)
    .\venv_name\Scripts\activate

    # Activate virtual environment (MacOS and Linux)
    source venv_name/bin/activate
    ```
* **Using conda (if you have Conda installed):**
    ```
    conda create --name venv_name
    conda activate venv_name
    ```


**3. Install Dependencies**

```
pip install ipykernel
cd Hack
pip install -r requirements.txt
```

**4. Open Jupyter Notebook in Visual Studio Code**

* Open up Visual Studio Code
* Open Folder (Ctrl + K, Ctrl + O)
* Navigate to and open the project folder '2D-Mapping-and-Simulation-Approach'
* Click on the 'Hack' folder and open analysis.ipynb
* You will be prompted to select a Python environment to run the notebook with, you should see your newly created virtual environment (if you created one). If not, use your Python installation of choice
* Follow prompts to install the Jupyter extension (if you haven't installed it for your environment before)

**5. Run the Jupyter Notebook**
* Hit Run All at the top of the notebook to reproduce all the charts and graphs we use in our solution!

## 3. Running the Web Application and 2D Mapping and Simulation 

This repository contains an AI simulation pipeline that generates predicted disaster data using three machine learning models. The predicted data from the development phase is already provided, so running the pipeline is optional. You can simply run the app if you prefer.

## Running the Web App

If you only want to run the web app:

1. **Create a Virtual Environment**
    * **Using venv :**
        ```
        # Install virtualenv (if you don't have it)
        pip install virtualenv

        # Create virtual environment
        python -m venv venv_name

        # Activate virtual environment (Windows)
        .\venv_name\Scripts\activate

        # Activate virtual environment (MacOS and Linux)
        source venv_name/bin/activate
        ```
    * **Using conda (if you have Conda installed):**
        ```
        conda create --name venv_name
        conda activate venv_name

2. **Change directory**
    - Change the directory to hack by using
        ```
        cd Hack
3. **Run the App**
   - Execute:
     ```bash
     python app.py
     ```
   - Look for the local host http://127.0.0.1 link in your console and open it in your browser.

## Running the AI Simulation Pipeline (Optional)

If you want to run the AI simulation pipeline (i.e., execute `main.ipynb`) in the ```./Prediction``` directory:

Note: The web application already containing the AI Simulation. This is just to run and overview the whole pipeline.

1. **Open the Notebook**
   - Open the `main.ipynb` file in your preferred IDE (e.g., Visual Studio Code).

2. **Select the Python Interpreter**
   - In Visual Studio Code, press `Ctrl + Shift + P` and type `Python: Select Interpreter`.
   - If the interpreter is not automatically listed, manually enter the path to your virtual environment’s Python executable:
     ```
     env/Scripts/python.exe
     ```
   - Re-select the kernel if needed.

3. **Run the Notebook**
   - Click the **Run All** button to execute all cells in the notebook.
   - **Note:** On an 8-core/16-thread CPU, the notebook may take approximately 10 minutes to finish running.

4. **Output**
   - The pipeline will generate predictions which are saved automatically into a JSON file with the following structure:
     ```json
     {
         "Total number of deaths": value,
         "Latitude": value,
         "Longitude": value,
         "Disaster type": value,
         "Disaster subtype": value
     }
     ```
   - Once the predictions are generated, you can run the app to view the results.

## Pipeline Overview (Optional)

The AI simulation pipeline consists of three sequential machine learning models:

1. **ARIMA Time-Series (First Model)**
   - Uses `statsmodels` for forecasting time-series data.

2. **Gaussian Process Regression (Second Model)**
   - Implemented with `scikit-learn`.

3. **Gradient Boosting Regression (Third Model)**
   - Also implemented with `scikit-learn`.

**Pipeline Flow:**
- The output of the ARIMA model is fed into the Gaussian Process regression model.
- The output of the Gaussian Process model is then used as input for the Gradient Boosting model.
- The final predictions from all three models are combined and stored in a JSON file for the app.

*Note:* Initially, the goal was to achieve real-time inference; however, due to slower inference times and limited development time, batch processing was implemented instead.

## Additional Information 

- If there is any configuration error please let us know through discord

Thank you! :)


