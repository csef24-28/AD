from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']

    if uname == "google" and passwrd == "google":
        return "Welcome %s" % uname
    else:
        return "Invalid credentials"

if __name__ == '__main__':
    app.run(debug=True)