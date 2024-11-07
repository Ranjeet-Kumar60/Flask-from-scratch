from flask import Flask
app=Flask(__name__)

@app.route("/home")
@app.route("/")
def Home():
    return "<h1>Welcome to our home page</h1>"


@app.route("/welcome/<name>")
def Lt(name):
    return f"<h1>Hi {name.title()}, welcome here </h1>"
    

if __name__ == "__main__":
    app.run(debug = True)