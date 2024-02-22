from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello',methods=['POST'])
def hello():
    mes = request.form['inputMassage']
    rm = ""
    for i in mes:
        rm += chr(ord(i)+3)
    
    return render_template('home.html', Result=f"{rm}")
if __name__ == "__main__":
    app.run()