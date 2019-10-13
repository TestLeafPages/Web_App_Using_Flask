from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def login_page():
    return render_template('Login_page.html')

@app.route('/home')
def home_page():
    return "Im Home Page"

@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    if request.method == "POST":
        print(request.form.get('NAME'))
        print(request.form.get('GMAIL'))
        print(request.form.get('PHONE'))
    return render_template("Register.html")


if __name__ == "__main__":
    app.run(debug = True)