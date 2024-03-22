from flask import Flask
from flask import render_template, request
from encryptionSelection import encryptionProsess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello',methods=['POST'])
def hello():
    message = request.form['inputMassage']
    encryptionType = request.form['encryptionType'] 
    #call encryption method
    encryptedMessage = encryptionProsess(message, encryptionType)
    return render_template('home.html', Result=f"{encryptedMessage}")
if __name__ == "__main__":
    app.run()