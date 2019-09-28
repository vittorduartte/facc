from flask import Flask, render_template, url_for, request, redirect, make_response
from datetime import datetime
import random, pdfkit

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    
    if request.method == 'POST':

        
        data = datetime.now()
        matricula = random.randrange(100000,999999)

        nome = request.form['nome']
        curso = request.form['curso']
        nivel = request.form['nivel']
        turno = request.form['turno']
        cidade = request.form['cidade']
        disciplinas = request.form['disciplinas']

        rendered = render_template('certificate.html', nome=nome.upper(), 
        data = data.strftime("%d/%m/%Y %H:%M"),
        matricula = data.strftime("%Y")+str(matricula),
        semestre = data.strftime("%Y"),
        curso=curso.upper(), 
        nivel=nivel.upper(), 
        turno=turno, 
        cidade=cidade.upper(), 
        disciplinas=range(0,int(disciplinas)), 
        num=disciplinas)

        pdf = pdfkit.from_string(rendered, False)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=certificado.pdf'

        return response  


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)