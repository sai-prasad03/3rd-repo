from flask import Flask

app  = Flask(__name__)

app.route('/')
def sai():
    return 'sonawane'

if __name__ == '__main__':
    app.run(debug=True)