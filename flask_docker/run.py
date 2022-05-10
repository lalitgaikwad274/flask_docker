from flask import Flask,render_template, request

app = Flask(__name__, template_folder = './')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def show():
    Name = request.form['name']

    return "Welcome to PUCSD " + Name 


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)