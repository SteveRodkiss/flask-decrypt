from flask import Flask, render_template, request
from encrypt import xor_encrypt, xor_decrypt
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/encypt/", methods=['GET','POST'])
def encrypt_page():
    if request.method == "POST":
        text = request.form['text']
        new_text = xor_encrypt(text)
        return render_template("encrypt.html", data=new_text)
    else:
        return render_template("encrypt.html")

@app.route("/decrypt/", methods=['GET','POST'])
def decrypt_page():
    if request.method == "POST":
        text = request.form['text']
        new_text = xor_decrypt(text)
        return render_template("decrypt.html", data=new_text)
    else:
        return render_template("decrypt.html")
