# Welcome to Dover Poly's March Hackathon Repository!

This README is split into 2 parts:

1.  Introduction to our solution
2.  Steps to reproduce our solution
    * a) Jupyter Notebook
    * b) Website

## 1. Introduction to our solution

**Hackathon Problem Statement:** "Analyse pertinent data trends concerning the biodiversity sector to improve the sector’s efficiency and abilities."

As the scope of the Hackathon problem statement is massive, we decided to craft our own problem statement (which is a subset of the hackathon's problem statement) so we could work on something that we are more passionate about and see our solution have direct impact.

**Our problem statement:** "How can we protect Endangered Species against Natural Disasters?"
(which is a subset of the hackathon's problem statement)

To tackle this we looked for relevant data online pertaining to these 2 topics and saw that we could analyze the data and glean useful information from historical data. But we wanted to go one step further and try and predict future data of some kind which would allow even more informed strategy and decision making, so that is what we did! :)

## 2. Steps to reproduce our solution

We have 2 parts to our solution:

* a) Analysis and Visualization of data on Endangered Species and Natural Disasters
* b) AI Geospatial Mapping and Simulation for Predictive Analysis of Natural Disasters

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
x