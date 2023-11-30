from sqlalchemy import create_engine, text
from flask import Flask, render_template, jsonify, request
from config import username, password, hostname, port, db
import pandas as pd



app = Flask(__name__)


engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{hostname}:{port}/{db}')

# Loop through all tables to get data from SQL to API
@app.route("/api/v1.0/flu_data")
def flu():
    table = ["fluvacc19", "fluvacc20", "fluvacc21", "fluvacc22"]
    df = []
    for i in table:
        query = f"SELECT * FROM {i}"
        conn = engine.connect()
        season = pd.read_sql(text(query), conn)
        df.append(season)
        conn.close()
    combined_df = pd.concat(df, ignore_index=True)
    return combined_df.to_json(orient="records")

# Get all the unique counties for the dropdown menu
@app.route("/api/v1.0/counties")
def counties():
    query = "SELECT distinct county FROM fluvacc_all ORDER BY county"
    conn = engine.connect()
    df = pd.read_sql(text(query), conn)
    conn.close()
    return df.to_json(orient="records")

# Create a route using a filter for counties based on user dropdown selection
@app.route("/api/v1.0/flu_data/<county>")
def county(county):
    query = f"SELECT flu_season, percentage_healthcare_professionals_vaccinated FROM fluvacc_all WHERE county = '{county}'"
    conn = engine.connect()
    df = pd.read_sql(text(query), conn)
    conn.close()
    return df.to_json(orient="records")

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)