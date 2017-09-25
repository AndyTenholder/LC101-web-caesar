from flask import Flask, request, render_template
from caesar import rot13


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['GET'])
def index():
    encrypted_message = ""
    if 'text' in request.args and 'rot' in request.args:
        rot = request.args.get('rot')
        rot = int(rot)
        message = request.args.get('text')
        encrypted_message = rot13(message,rot)
        
    return render_template('web_caesar.html', text = encrypted_message)

@app.route("/" , methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    message = request.form['text']
    encrypted_message = rot13(message,rot)

    return render_template('web_caesar.html', text = encrypted_message)

app.run()