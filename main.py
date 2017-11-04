from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <!-- create your form here -->
                <form action="/caesar" method="post" id="usrform">
                    <label for="rotation">
                        Number to rotate by: 
                        <input type="text" id="rotation" name="rot" value="0"/>
                    </label>
                    <textarea name="text" form="usrform"></textarea>
                    <input type="submit" value="Encrypt"/>
                </form>      
        </body>
    </html>
"""
@app.route("/")

def index():
    return form

@app.route("/caesar", methods=["POST"])
def encrypt():
    rot_num = int(request.form['rot'])
    message = request.form['text']

    message = rotate_string(message, rot_num)
    return "<h1>" + message + "</h2>"

app.run()