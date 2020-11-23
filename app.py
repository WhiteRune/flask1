from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

key = b'bzQzIX4gp5dfBC79P5OLoqqJdwvA6yqJ2nvA3NLX4Us='
f = Fernet(key)


@app.route('/encrypt')
def encrypt():
    """
    Shows text in encrypted view
    """
    string = request.args.get("string")
    if not string:
        name = ''
        token = "Произошли технические шоколадки, не обнаружена строка."
    else:
        name = 'Encrypted result:'
        string = string.encode('utf-8')
        token = (f.encrypt(string)).decode()
    return render_template('index.html', result=token, name=name)


@app.route('/decrypt')
def decrypt():
    """
    Shows text in decrypted view
    """
    token = request.args.get("string")
    if not token:
        name = ''
        string = "Произошли технические шоколадки, не обнаружена строка."
    else:
        name = 'Decrypted result:'
        token = token.encode('utf-8')
        string = (f.decrypt(token)).decode()
    return render_template('index.html', result=string, name=name)


app.run(debug=True)

