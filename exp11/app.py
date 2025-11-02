from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    uname = request.args.get('uname')
    passwrd = request.args.get('pass')

    if uname == "google" and passwrd == "google":
        return "Data Retrieved %s" % uname
    else:
        return "Invalid Credentials"

if __name__ == '__main__':
    app.run(debug=True)