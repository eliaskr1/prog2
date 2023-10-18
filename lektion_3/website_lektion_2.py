from flask import Flask, render_template
import pandas as pd
import urllib
import numpy as np
# import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import urllib.request
import ssl

app = Flask(__name__)

@app.get("/")
def get_plotly():

    # Skapa ett context som säger att vi väljer att lita på detta API
    context = ssl._create_unverified_context()

    # Pandas
    ## Lägg url i en variabel för att göra koden mer lättläst
    data_url = "https://polisen.se/aktuellt/rss/stockholms-lan/handelser-rss---stockholms-lan/"
    ## Läs innehållet som returneras från den URL:en RSS==XML
    rss = urllib.request.urlopen(data_url, context=context).read()
    ## Lär RSS in i ett Pandas dataframe
    df = pd.read_xml(rss, xpath="//item")
    ## Hämta en HTML-representation av tabellen
    table = df.to_html(columns=['description', 'link'], justify='left', classes="table table-striped", render_links=True)
    ## Skapa en ny column utan timestamp, dvs. endast de 16 första tecknen
    df['date'] = df['pubDate'].apply(lambda x: x[:16])

    # Plotly
    ## Skapa ett Bar Diagram av värdena i kolumnen date 
    fig = px.bar(data_frame=df['date'])
    ## Spara diagrammet som HTML
    diagram = fig.to_html(full_html=False) 

    # Returnera resultatet
    #return diagram
    return render_template('plotly.htm', data=diagram, table=table, title='Ett exempel på hur man kan skapa layout med Bootstrap')
