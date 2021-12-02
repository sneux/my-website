from flask import Flask, redirect, url_for

app = Flask(__name__)
# this is the root of the page
# route connects the url to the page 
@app.route("/")
def home_page():
    return "index page"

@app.route("/admin")
def admin():
    return redirect(url_for("home_page"))

if __name__ == "__main__":
    app.run()

@app.route("/hi/")
def who():
    return "Who are you?"

@app.route("/hi/<username>/")
def greet(username):
    return f"Hi, {username}!"