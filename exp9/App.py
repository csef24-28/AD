from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

def random_image():
    img_dir = "./static"
    img_list = os.listdir(img_dir)
    return random.choice(img_list)

@app.route('/', methods=["GET", "POST"])
def index():
    image = random_image()
    return render_template('home.html', home_image=image)

@app.route('/register', methods=["GET", "POST"])
def register():
    return render_template('registration.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)