from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome To Future of AI'


if __name__ ==  '__main__':
    app.run(debug = True)
    


