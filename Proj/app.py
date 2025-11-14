from flask import Flask, flash, redirect, render_template, request, jsonify, url_for, session
import psycopg2 #install: pip install psycopg2

#DB connection from config
app = Flask(__name__)

# Connect to the database         //replace with your local db name
conn = psycopg2.connect(database="flask_carrental_db", user="postgres",
                        password="new_password", host="localhost", port="5432")
                        #set to your password



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/locations')
def locations():
    return render_template('locations.html')

if __name__ == '__main__':
    app.run()