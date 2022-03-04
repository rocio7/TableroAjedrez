from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def index():
    return  render_template('index.html',filas=8,columnas=8,color1='red',color2='black')

@app.route('/<int:x>')
def filas(x):
    return render_template('index.html',filas=x,columnas=8,color1='red',color2='black')

@app.route('/<int:x>/<int:y>')
def filas_columnas(x,y):
    return render_template('index.html',filas=x,columnas=y,color1='red',color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>')
def filas_columnas_color1(x,y,color1):
    return render_template('index.html',filas=x,columnas=y,color1=color1,color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def filas_columnas_color2(x,y,color1,color2):
    return render_template('index.html',filas=x,columnas=y,color1=color1,color2=color2)


if __name__== "__main__":
    app.run(debug=True)
