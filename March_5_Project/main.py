from wsgiref import simple_server
from flask import Flask, request, render_template
import flask_monitoringdashboard as dashboard
import pandas as pd
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request
import seaborn as sns
import matplotlib.pyplot as plt


from checkAPI import get_disease

app = Flask(__name__)
dashboard.bind(app)
CORS(app)

df=pd.read_csv("C:\\Users\\MCS\\Downloads\\diabetes.csv")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/getData')
def get_disease_data():
    #disease = request.args.get('disease')

    # if not bool(disease.strip()):
    #     disease="diabetes"


    disease_data=get_disease()
    return render_template("index.html")


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 2000
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()