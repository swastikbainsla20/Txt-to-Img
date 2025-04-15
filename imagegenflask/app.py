from flask import Flask
from flask import render_template
import openai
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/About")
def about():
    return render_template("about.html")

@app.route("/generateimages")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
