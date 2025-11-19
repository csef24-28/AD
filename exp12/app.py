from flask import Flask, request, render_template

app = Flask(__name__)

qa = {}
for line in open("questions.txt"):
    q, a = line.strip().split(":", 1)
    qa[q.lower()] = a

@app.route("/", methods=["GET","POST"])
def chat():
    ans = ""
    if request.method == "POST":
        q = request.form["q"].lower()
        ans = qa.get(q, "I don't know this.")
    return render_template("chat.html", ans=ans)

app.run()
