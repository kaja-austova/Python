from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_def():
    return render_template("neco.html", title="Jídelníček", den = "Jídelníček")

@app.route('/pondeli')
def pondeli_def():
    # return render_template("web.html", title="Pondělí", den = "Pondělí", text = "Přejeme Vám hezký začátek týdne.", tabulka = "https://docs.google.com/spreadsheets/d/1JpEUpUJ3slFP1y2PgJV1J_2_sBf5VOek4TUcq90P_Cs/edit#gid=0")
    return render_template("web.html", title="Pondělí", den = "Pondělí", text = "Přejeme Vám hezký začátek týdne.", bunka_start="A6", bunka_konec="G10")

@app.route('/utery')
def utery_def():
    return render_template("web.html", title="Úterý", den = "Úterý", text = "To nejhorší máte za sebou.", bunka_start="A12", bunka_konec="G17")

@app.route('/streda')
def streda_def():
    return render_template("web.html", title="Středa", den = "Středa", text = "Už jste v polovině!", bunka_start="A20", bunka_konec="G24" )

@app.route('/ctvrtek')
def čtvrtek_def():
    return render_template("web.html", title="Čtvrtek", den = "Čtvrtek", text = "Před Vámi je cílová rovinka.", bunka_start="A27", bunka_konec="G31")

@app.route('/patek')
def patek_def():
    return render_template("web.html", title="Pátek", den = "Pátek", text = "Ten všemi očekávaný den je tu.", bunka_start="A34", bunka_konec="G38" )