from flask import Flask,request,render_template

app = Flask(__name__)



@app.route('/home')
def home():
    return render_template('home_page.html')

@app.route('/add',methods = ['GET'])
def add():
    input_1 = int(request.args.get('a'))
    input_2 = int(request.args.get('b'))
    sum = input_1 + input_2
    return str(sum)

if __name__ == '__main__':
    app.run(debug = True)