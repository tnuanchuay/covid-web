from flask import Flask
from flask_cors import CORS
from tensorflow.keras.models import Model, load_model
import pandas as pd
import json
import numpy as np 
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from datetime import timedelta
from datetime import datetime

error_consts = [2.280747636, 3.976510794, 4.792487913, 13.64721209]

IntervalDays = 50

app = Flask(__name__)
CORS(app)

def loadData():
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
    df = df.fillna(0)
    return df

print("!!! Loading dataset")
df = loadData()
columns = df.columns.values

print("!!! Loading models")
model7 = load_model('pre-train/new-vac-1H-7')
model14 = load_model('pre-train/new-vac-1H-14')
model21 = load_model('pre-train/new-vac-1H-21')
model28 = load_model('pre-train/new-vac-1H-28')

print("!!! Forecasting")
totalCaseScaler = StandardScaler()
totalCaseScaler.fit(df["total_cases"].values.reshape(-1, 1))
df["total_cases_norm"] = totalCaseScaler.transform(df["total_cases"].values.reshape(-1, 1)).flatten()

totalVacScaler = StandardScaler()
totalVacScaler.fit(df["total_vaccinations"].values.reshape(-1, 1))
df["total_vaccinations_norm"] = totalVacScaler.transform(df["total_vaccinations"].values.reshape(-1, 1)).flatten()

X = []
Y = []
tcn = df[df["location"] == "Thailand"]["total_cases_norm"].values
tvn = df[df["location"] == "Thailand"]["total_vaccinations_norm"].values

for i in range(0, len(tcn)-IntervalDays):
    tcnx = tcn[i:i+IntervalDays]
    tvnx = tvn[i:i+IntervalDays]
    x = np.array([tcnx, tvnx]).T
    X.append(x)

X = np.array(X).reshape(-1, IntervalDays, 2)
P7 = model7.predict(np.array([X[-1]]))
P7=totalCaseScaler.inverse_transform(P7)[0][0]
print(P7)
P14 = model14.predict(np.array([X[-1]]))
P14 = totalCaseScaler.inverse_transform(P14)[0][0]
print(P14)
P21 = model21.predict(np.array([X[-1]]))
P21 = totalCaseScaler.inverse_transform(P21)[0][0]
print(P21)
P28 = model28.predict(np.array([X[-1]]))
P28 = totalCaseScaler.inverse_transform(P28)[0][0]
print(P28)

@app.route("/data")
def date():
    data = []
    for row in df[df["location"] == "Thailand"].values:
        data.append({
            'date': row[list(df.columns.values).index('date')],
            'cases': row[list(df.columns.values).index('total_cases')]
        })

    data[-1]["prediction"] = list([data[-1]["cases"], data[-1]["cases"]])
    currentDate = datetime.fromisoformat(data[-1]["date"])
    data.append({
        "date": (currentDate + timedelta(days=7)).strftime("%Y-%m-%d"),
        "prediction": list([int(P7*(100+error_consts[0])/100), int(P7*(100-error_consts[0])/100)])
    })
    data.append({
        "date": (currentDate + timedelta(days=14)).strftime("%Y-%m-%d"),
        "prediction": list([int(P14*(100+error_consts[1])/100), int(P14*(100-error_consts[1])/100)])
    })
    data.append({
        "date": (currentDate + timedelta(days=21)).strftime("%Y-%m-%d"),
        "prediction": list([int(P21*(100+error_consts[2])/100), int(P21*(100-error_consts[2])/100)])
    })
    data.append({
        "date": (currentDate + timedelta(days=28)).strftime("%Y-%m-%d"),
        "prediction": list([int(P28*(100+error_consts[3])/100), int(P28*(100-error_consts[3])/100)])
    })

    data = data[-10:]

    return json.dumps({'data':list(data)})


@app.route("/reset-df")
def resetdf():
    df = loadData()
    totalCaseScaler = StandardScaler()
    totalCaseScaler.fit(df["total_cases"].values.reshape(-1, 1))
    df["total_cases_norm"] = totalCaseScaler.transform(df["total_cases"].values.reshape(-1, 1)).flatten()

    totalVacScaler = StandardScaler()
    totalVacScaler.fit(df["total_vaccinations"].values.reshape(-1, 1))
    df["total_vaccinations_norm"] = totalVacScaler.transform(df["total_vaccinations"].values.reshape(-1, 1)).flatten()
    X = []
    Y = []
    tcn = df[df["location"] == "Thailand"]["total_cases_norm"].values
    tvn = df[df["location"] == "Thailand"]["total_vaccinations_norm"].values

    for i in range(0, len(tcn)-IntervalDays):
        tcnx = tcn[i:i+IntervalDays]
        tvnx = tvn[i:i+IntervalDays]
        x = np.array([tcnx, tvnx]).T
        X.append(x)

    X = np.array(X).reshape(-1, IntervalDays, 2)
    P7 = model7.predict(np.array([X[-1]]))
    P7=totalCaseScaler.inverse_transform(P7)[0][0]
    print(P7)
    P14 = model14.predict(np.array([X[-1]]))
    P14 = totalCaseScaler.inverse_transform(P14)[0][0]
    print(P14)
    P21 = model21.predict(np.array([X[-1]]))
    P21 = totalCaseScaler.inverse_transform(P21)[0][0]
    print(P21)
    P28 = model28.predict(np.array([X[-1]]))
    P28 = totalCaseScaler.inverse_transform(P28)[0][0]
    print(P28)
    return json.dumps([int(P7), int(P14), int(P21), int(P28)])