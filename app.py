from flask import Flask, url_for, redirect, render_template, url_for, session, logging, request



app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
