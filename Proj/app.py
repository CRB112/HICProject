from flask import Flask, flash, redirect, render_template, request, jsonify, url_for, session
import config

#DB connection from config
app = Flask(__name__)
app.secret_key = config.SECRET_KEY

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()