from flask import Flask, redirect, render_template, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/project1")
def project1():
    return render_template('project1.html')

@app.route("/project2")
def project2():
    return render_template('project2.html')


if __name__ == "__main__":
    app.run(debug=False)