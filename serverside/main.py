from flask import Flask
from flask_cors import CORS
from tensorflow.keras.models import Model, load_model
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

def loadData():
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
    df = df.fillna(0)
    print(columns)
    return df

print("!!! Loading dataset")
df = loadData()
columns = df.columns.values

print("!!! Loading models")
model7 = load_model('pre-train/new-vac-1H-7')


@app.route("/data")
def date():
    data = []
    for row in df[df["location"] == "Thailand"].values:
        data.append({
            'date': row[list(df.columns.values).index('date')],
            'cases': row[list(df.columns.values).index('total_cases')]
        })
    return json.dumps({'data':data})


@app.route("/reset-df")
def resetdf():
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")