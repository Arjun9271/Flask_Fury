from flask import Flask

app = Flask(__name__)


@app.route('/about')
def home():
    return 'THIS IS HOME PAGE'

@app.route('/magic')
def add():
    a = 2
    b = 3
    sum = a+b
    return str(sum)



if __name__ == '__main__':
   app.run(debug = True)