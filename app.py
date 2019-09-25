from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    var = "Minha aplicação Flask!"
    return render_template('index.html', var = var)

@app.route('/tool/', methods = ['GET', 'POST'])
def tool():
    
    if request.method == 'POST':

        nome = request.form['nome']
        curso = request.form['curso']
        nivel = request.form['nivel']
        
        return render_template('certificate.html', nome=nome.upper(), curso=curso.upper(), nivel=nivel.upper())

    return render_template('tool.html')

if __name__ == '__main__':
    app.run(debug = True)