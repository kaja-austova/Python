from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pondeli')
def hello_world():
    return render_template("web.html", title="Pondělí", den = Pondělí, text = "Přejeme Vám hezký začátek týdne.", tabulka = "https://docs.google.com/spreadsheets/d/1JpEUpUJ3slFP1y2PgJV1J_2_sBf5VOek4TUcq90P_Cs/pubhtml/sheet?headers=false&amp;gid=0&amp;range=A6:G10")
