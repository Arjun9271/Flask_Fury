from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/login')
def home():
    return render_template('details.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug = True)