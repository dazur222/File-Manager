from flask import Flask, render_template, request
from bubble_sort import imprimir_txt, count_palabra, count_renglones, count_palabras, write_file, ordenAlfabetico, palabras_unicas, palabra_mas_larga, remove_text

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search")
def searchboy():
    file = request.args.get("files")
    return render_template('index.html', result=imprimir_txt(file+".txt"))

@app.route("/overWrite")
def writeboi():
    file = request.args.get("overwrite")
    mots = request.args.get("overwrite-input")
    return render_template('index.html', result=write_file(file+".txt", " "+mots))

@app.route("/remove")
def remove():
    file = request.args.get("remove")
    return render_template('index.html', result=remove_text(file+".txt"))

@app.route("/count")
def countMots():
    file = request.args.get("file-count")
    mot = request.args.get("count-input")
    return render_template('index.html', result= count_palabra(mot, file+".txt"))

@app.route("/countLines")
def countLines():
    file = request.args.get("CountLines")
    return render_template('index.html', result=count_renglones(file+".txt"))

@app.route("/countWords")
def countWords():
    file = request.args.get("CountWords")
    return render_template('index.html', result=count_palabras(file+".txt"))

@app.route("/ordenar")
def ordenar():
    file = request.args.get("order")
    return render_template('index.html', result=ordenAlfabetico(file+".txt"))

@app.route("/unicas")
def unicas():
    file = request.args.get("unicas")
    return render_template('index.html', result=palabras_unicas(file+".txt"))

@app.route("/longest")
def longest():
    file = request.args.get("longest")
    return render_template('index.html', result=palabra_mas_larga(file+".txt"))

if __name__ == ("__main__"):
    app.run(debug=True)
