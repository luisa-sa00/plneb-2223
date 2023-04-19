from flask import Flask, render_template
import json

app = Flask(__name__)

file = open("dicionario_medico_pt_en.json", encoding='utf-8')
db = json.load(file)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/terms")
def terms():
    return render_template("terms.html", designations=db.keys())


@app.route("/term/<t>")
def term(t):
    return render_template("term.html", designation=t, value=db.get(t, "None"))


app.run(host="localhost", port=4000, debug=True)