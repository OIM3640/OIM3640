from flask import Flask

app = Flask(__name__)


# Home route
@app.route("/")
def homepage():
    return "This is the homepage!"


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        return f"Hello, {name}!"
    return "Hello from the /hello route!"


if __name__ == "__main__":
    app.run(debug=True)
