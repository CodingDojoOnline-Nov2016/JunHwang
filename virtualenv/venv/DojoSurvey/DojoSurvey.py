from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
    return render_template("DojoSurvey.html")

@app.route('/users', methods=['POST'])
def create_user():
        data = request.form
        print data
        return render_template("users.html", data = data)

if __name__ == '__main__':
    app.run(debug = True)
