from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def indeks():
    return render_tamplate("index.html", spr = "gg")
    # return "<p>Hello, World!</p>"

app.route("/LoveCalc", methods =["POST"])
def LoveCalc():
    tmp=dict(request.form)
    ime1=tmp.get("ime1")
    ime2=tmp.get("ime2")
    return render_template("index.html")
    return f"{ime1} + {ime2} = {random.int(0, 100)}%"


app.run(debug = True)