from flask import Flask, request
from caesar import rot13

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/" method="get">
            <label for="rotation">Rotate by:</label>
            <input id="rotation" type="text" name="rot" value="0"/>
            <textarea id="text_to_encrypt" name="text" rows="10" cols="50">{0}</textarea>
            <input type="submit" value ="encrypt using GET"/>
            <input type="submit" formmethod="post" formaction="/" value='encrypt using POST'/>
        </form>
    </body>

</html>
"""

@app.route("/", methods=['GET'])
def index():
    encrypted_message = ""
    if 'text' in request.args and 'rot' in request.args:
        rot = request.args.get('rot')
        rot = int(rot)
        message = request.args.get('text')
        encrypted_message = rot13(message,rot)
    return form.format(encrypted_message)

@app.route("/" , methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    message = request.form['text']
    encrypted_message = rot13(message,rot)

    return form.format(encrypted_message)

app.run()