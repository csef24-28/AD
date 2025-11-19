from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["user"]
        p = request.form["pass"]
        if u == "admin" and p == "123":
            return f"Welcome {u}"
        return "Invalid login"
    return render_template("login.html")

app.run()
