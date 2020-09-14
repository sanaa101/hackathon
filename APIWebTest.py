from flask import Flask
from backgroundCode import go
app = Flask(__name__)

@app.route ("/")
def hello ():
    return (go())
 
if (__name__ =="__ main__"):
    app.debug = True
    app.run ()

