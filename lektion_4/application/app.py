from flask import Flask, render_template, request
import urllib.request
import ssl
import json
import pandas as pd
import werkzeug

app = Flask(__name__)

@app.route("/")
def index():
    '''kommentar'''
    # Kod
    return render_template("index.html")

@app.route("/form")
def form():
    '''kommentar'''
    # Kod
    return render_template("form.html")

# @app.post("/api")
@app.route("/api", methods=["POST"])
def api_post():
    '''kommentar'''
    
    
    year = request.form["year"]
    country_code = request.form["countrycode"]
    
    context = ssl._create_unverified_context() 
    data_url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}" 
    json_data = urllib.request.urlopen(data_url, context=context).read() 
    data = json.loads(json_data)
    df = pd.DataFrame(data)
    table_data = df.to_html(columns=["date", "localName"], classes="table table-hover table-striped", justify="left")
    
    return render_template("index.html", data=table_data)

    
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

if __name__ == "__main__":
    app.run(debug=True)
