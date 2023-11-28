from sqlalchemy import create_engine, text
from flask import Flask, render_template, jsonify, request
from config1819 import username, password, hostname, port, db
import pandas as pd



app = Flask(__name__)


engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db}')

# Loop through all tables to get data from SQL to API
@app.route("/api/v1.0/flu_data")
def flu(countyIn):
    #table = ["fluvacc19", "fluvacc20", "fluvacc21", "fluvacc22"]
    df = []
    #for i in table:
        #query = f"SELECT * FROM {i}"
    query = f"SELECT * FROM fluvacc_all WHERE county = {countyIn}"
    conn = engine.connect()
    season = pd.read_sql(text(query), conn)
    df.append(season)
    conn.close()
    combined_df = pd.concat(df, ignore_index=True)
    return combined_df.to_json(orient="records")

@app.route("/api/v1.0/counties")
def counties():
    #table = ["fluvacc19", "fluvacc20", "fluvacc21", "fluvacc22"]
    df = []
    #for i in table:
    query = "SELECT distinct county FROM fluvacc_all ORDER BY county"
    conn = engine.connect()
    season = pd.read_sql(text(query), conn)
    df.append(season)
    conn.close()
    combined_df = pd.concat(df, ignore_index=False)
    return combined_df.to_json(orient="records")

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    # TO DO - get data from database
    # TO DO - pass data  to clean using sql query 
    # CONVERT TO A BUNCH OF LISTS 

    # SEND TO DASHBOARD.HTML
    data = {
        "yaxis" : [0,10,20,30],
        "xaxis" : ["2018-2019", "2020-2021", "2021-2022", "2022-2023"],
    }

    return render_template("dashboard.html")


# @app.route("/api/v1.0/sumpetals")
# def sumpetaliris():
#     conn = engine.connect()
#     query = "SELECT SUM(petalwidthcm) as petalwidth, SUM(petallengthcm) as petallength FROM iris"
#     df = pd.read_sql(query, conn)
#     return df.to_json(orient="records")


if __name__ == "__main__":
    app.run(debug=True, port=5000)