from flask import Flask, render_template
import pandas as pd

data = {
    "Landsdel": ["Götaland", "Götaland", "Götaland", "Svealand", "Svealand", "Norrland", "Norrland", "Norrland", "Norrland", "Norrland"],
    "Landskap": ["Östergötland", "Östergötland", "Västergötland", "Södermanland", "Södermanland", "Norrbotten", "Gästrikland", "Ångermanland", "Ångermanland", "Ångermanland"],
    "Stad": ["Linköping", "Motala", "Mjölby", "Mariefred", "Nyköping", "Piteå", "Sandviken", "Sollefteå", "Kramfors", "Örnsköldsvik"]
}

df = pd.DataFrame(data)

html = df.to_html(classes="table table-hover table-dark table-striped", justify="left")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("data.html", data=html)

if __name__ == '__main__':
    app.run(debug=True)
