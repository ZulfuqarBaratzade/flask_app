from flask import Flask, render_template


app = Flask(__name__)



#Routing
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def Register():
    return render_template("register.html")
@app.route("/login")
def Login():
    return render_template("login.html")
@app.route("/blogs")
def Blog():
    return render_template("blog.html")
@app.route("/contact")
def Contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
