from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    var = "Minha aplicação Flask!"
    return render_template('index.html', var = var)

@app.route('/certificate/')
def cert():

    return render_template('certificate.html')


if __name__ == '__main__':
    app.run(debug = True)