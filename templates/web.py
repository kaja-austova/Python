from flask import Flask, render_template

app = Flask(__name__)

@app.route('/pondeli')
def pondeli_def():
    return render_template("web.html", title="Pondělí", den = Pondělí, text = "Přejeme Vám hezký začátek týdne.", tabulka = "https://docs.google.com/spreadsheets/d/1JpEUpUJ3slFP1y2PgJV1J_2_sBf5VOek4TUcq90P_Cs/pubhtml/sheet?headers=false&amp;gid=0&amp;range=A6:G10")

@app.route('/utery')
def utery_def():
    return render_template("web.html", title="Úterý", den = Úterý, text = "To nejhorší máte za sebou.", tabulka = "https://docs.google.com/spreadsheets/d/1JpEUpUJ3slFP1y2PgJV1J_2_sBf5VOek4TUcq90P_Cs/pubhtml/sheet?headers=false&amp;gid=0&amp;range=A6:G10")

@app.route('/streda')
def streda_def():
    return render_template("web.html", title="Středa", den = Středa, text = "Už jste v polovině!", tabulka = "https://docs.google.com/spreadsheets/d/1JpEUpUJ3slFP1y2PgJV1J_2_sBf5VOek4TUcq90P_Cs/pubhtml/sheet?headers=false&amp;gid=0&amp;range=A6:G10")

@app.route('/ctvrtek')
def čtvrtek_def():
    return render_template("web.html", title="Čtvrtek", den = Čtvrtek, text = "Před Vámi je cílová rovinka.", tabulka = "https://docs.google.com/spreadsheets/d/1JpEUpUJ3slFP1y2PgJV1J_2_sBf5VOek4TUcq90P_Cs/pubhtml/sheet?headers=false&amp;gid=0&amp;range=A6:G10")

@app.route('/patek')
def patek_def():
    return render_template("web.html", title="Pátek", den = Pátek, text = "Ten všemi očekávaný den je tu.", tabulka = "https://docs.google.com/spreadsheets/d/1JpEUpUJ3slFP1y2PgJV1J_2_sBf5VOek4TUcq90P_Cs/pubhtml/sheet?headers=false&amp;gid=0&amp;range=A6:G10")
