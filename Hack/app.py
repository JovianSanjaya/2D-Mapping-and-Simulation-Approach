from flask import Flask, render_template, redirect, url_for
import pandas as pd
import matplotlib as plt

app = Flask(__name__)

@app.route("/data_analysis")
def data_analysis():
    return render_template("data_analysis.html")

@app.route("/ai_prediction")
def ai_prediction():
    return render_template("ai_prediction.html")

@app.route("/")
def home():
    return redirect(url_for('data_analysis'))

if __name__ == "__main__":
    app.run(debug=True)
