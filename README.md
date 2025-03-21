# Dover Poly's Repository for BuildingBlocs Hackathon 

This README is split into 2 parts:

1.  Introduction to our solution
2.  Steps to reproduce our solution
    * a) Jupyter Notebook
    * b) Web Application with 2D AI Geospatial Mapping and Simulation

## 1. Introduction and Overview

**Hackathon Problem Statement:** "Analyse pertinent data trends concerning the biodiversity sector to improve the sector’s efficiency and abilities."

As the scope of the Hackathon problem statement is massive, we decided to craft our own problem statement (which is a subset of the hackathon's problem statement) so we could work on something that we are more passionate about and see our solution have direct impact.

**Our problem statement:** "How can we protect Endangered Species against Natural Disasters?"
(which is a subset of the hackathon's problem statement)

To tackle this we looked for relevant data online pertaining to these 2 topics and saw that we could analyze the data and glean useful information from historical data. But we wanted to go one step further and try and predict future data of some kind which would allow even more informed strategy and decision making, so that is what we did! :)

Hence our solution has a two-pronged approach, data analysis and prediction. And by combining both we can come up with more effective strategies to protect endangered species against natural disasters. In the data analysis portion, we use a Jupyer Notebook to do explolatory data analysis and identify key trends and correlations on our natural disaster and endangered species data. In the prediction portion, we use a pipeline of 3 models - ARIMA, Gaussian Process Regression and Gradient Boosting Regression to forecast disaster data, which can geospatial data. To wrap it all up, we combine all the generated plots and charts into a website and then also integrate an interactive 2D map to visualize the predicted natural disaster time, location and severity. This enables informed decision-making and targeted conservation efforts, ultimately contributing to the preservation of biodiversity.

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

**2. (Recommended) Create and activate Python Virtual Environment**
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

    # If "cannot be loaded because running scripts is disabled on this system" error occurs, 
    # run "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process" before activating virtual environment.
    
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

1. **Create a Virtual Environment (if haven't make one)**
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

        # If "cannot be loaded because running scripts is disabled on this system" error occurs, 
        # run "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process" before activating virtual environment.
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


## Citations


**ARIMA Time-Series:**

* Box, G. E. P., & Jenkins, G. M. (1970). Time Series Analysis: Forecasting and Control. San Francisco: Holden-Day.
* statsmodels.tsa.arima.model.ARIMA: [https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)
* Google Books: Time Series Analysis: [https://books.google.com.sg/books/about/Time_Series_Analysis.html?id=5BVfnXaq03oC&redir_esc=y](https://books.google.com.sg/books/about/Time_Series_Analysis.html?id=5BVfnXaq03oC&redir_esc=y)

**Gaussian Process Regressor:**

* Williams, C. K. I., & Rasmussen, C. E. (1996). Gaussian Processes for Regression. In Advances in Neural Information Processing Systems 8 (pp. 514–520). MIT Press.
* scikit-learn Gaussian Process: [https://scikit-learn.org/stable/modules/gaussian_process.html](https://scikit-learn.org/stable/modules/gaussian_process.html)
* Aston Publications: [https://publications.aston.ac.uk/id/eprint/651/](https://publications.aston.ac.uk/id/eprint/651/)
* ACM Digital Library: [https://dl.acm.org/doi/10.5555/3586589.3586821](https://dl.acm.org/doi/10.5555/3586589.3586821)

**Gradient Boosting Regressor:**

* Friedman, J. H. (2001). Greedy Function Approximation: A Gradient Boosting Machine. The Annals of Statistics, *29*(5), 1189–1232. [https://doi.org/10.1214/aos/1013203451](https://doi.org/10.1214/aos/1013203451)
* scikit-learn Gradient Boosting Regressor: [https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingRegressor.html)
* Wikipedia: Gradient Boosting: [https://en.wikipedia.org/wiki/Gradient_boosting](https://en.wikipedia.org/wiki/Gradient_boosting)

**Datasets:**

* EM-DAT: The International Disaster Database: [https://www.emdat.be/](https://www.emdat.be/)
* NASA Earthdata: SEDAC CIESIN SEDAC PEND GDIS 1.00: [https://www.earthdata.nasa.gov/data/catalog/sedac-ciesin-sedac-pend-gdis-1.00](https://www.earthdata.nasa.gov/data/catalog/sedac-ciesin-sedac-pend-gdis-1.00)
* CIESIN Columbia University: GDIS Codebook: [https://ciesin.columbia.edu/data/gdis-1960-2018/gdis-codebook-june2020.psdf](https://ciesin.columbia.edu/data/gdis-1960-2018/gdis-codebook-june2020.pdf)

## Technology Stack
* [NumPy](https://numpy.org/doc/stable/) 
* [Pandas](https://pandas.pydata.org/docs/)
* [Matplotlib](https://matplotlib.org/stable/contents.html)
* [Scikit-learn](https://scikit-learn.org/stable/user_guide.html)
* [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [Folium](https://python-visualization.github.io/folium/)
* [Rasterio](https://rasterio.readthedocs.io/en/stable/)

