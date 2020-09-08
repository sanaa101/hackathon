from flask import Flask

app = Flask(__name__)

@app.route ("/")
def hello ():
    def print_statement  ():
        print ('I hate mom',
                'I really hate mom')
    return print_statement()

if (__name__ =="__ main__"):
    app.debug = True
    app.run ()

