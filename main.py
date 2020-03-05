from flask import Flask, render_template, request, make_response, redirect, url_for
from models import User, db

app = Flask(__name__)
db.create_all()  # create (new) tables in the database

@app.route ("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)
