from flask import Flask
import uuid


app = Flask(__name__)
my_id = str(uuid.uuid4())

# open a flask route /
@app.route("/")

def hello_world():   
    """
    function return a hello at connection
    """
    sentence = '<p>Hello World! '+my_id+' <p>'
    return sentence

# open a flask route /bye
@app.route("/bye")
def bye():
    """
    function return a bye at route /bye
    """
    return "<p>Bye World! <p>"

# run the flask server on port in debug
app.run(debug=True,port=5000, host='0.0.0.0')
