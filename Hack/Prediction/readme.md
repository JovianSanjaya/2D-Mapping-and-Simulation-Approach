This is the readme for running the AI simulation pipeline (main.ipynb).
This part is optional to run, as this repository comes with our own predicted data from development.

If you only want to run the app, simple create a virtual environment and run app.py in the Hack folder.

Creating the virtual environment:
1. Head to the main folder "2D-Mapping-and-Simulation-Approach"
2. Follow the commands below to set up the virtual environment (Note: try to have python3.10 and above on your local machine)
    - pip install virutalenv
    - virutalenv env
    - cd env/Scripts
    - activate
    - cd ..
    - cd ..
    - pip install -r Hack/requirements.txt
3. Afterwards, run the app using
    - python app.py
    Look for the generated url link and open it in a browser of your choice

If you want to run the AI simulation pipeline, follow the additional steps below:
1. Open up the .ipynb in an IDE of your choice (I am using visual studio code in this case)
2. Select the python interpreter in the created virtual environment from earlier as your kernel
    - Note: If you cannot find the python interpreter, in visual studio code, press the ctrl + shift + p keys,
    type "python select interpreter". There, you should see the option to enter the interpreter path manually.
    The interpreter path for the virtual environment should be env/Scripts/python.exe. Afterwards, try selecting
    the kernel again, it should show up automatically this time.
3. Press the "Run All" button to run the jupyter notebook.
    - Note: The jupyter notebook would take some time to run finish. On a 8 core 16 threads cpu, it took about 10 minutes
    to fully run finish.
4. The predictions generated will be automatically saved and you can go ahead and run the app.

Brief explanation of the AI simulation pipeline:
- The pipeline consists of three different machine learning models:
    - First model: ARIMA time-series from statsmodels
    - Second model: Guassian Process regression from scikit-learn
    - Third model: Gradient Boosting regression from scikit-learn
- The pipeline starts with the first model, following by the second and lastly the third.
- The output from the first model gets feeded into the second model, and the output from the second model gets feeded
into the third model, hence I called it a pipeline.
- The end output from the pipeline consists of the predictions from all three models, stored inside a json file for use by the app.
{
    "Total number of deaths": value,
    "Latitude": value,
    "Longitude": value,
    "Disaster type": value,
    "Disaster subtype": value
}
- I initially wanted it to be real-time inference, but the inference time taken was a bit slow, also I had not enough time to
work on it.