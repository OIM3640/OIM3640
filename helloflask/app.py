from flask import Flask, render_template
from weather import get_temp

app = Flask(__name__)


@app.route(
    "/"
)  # if the domain is aryan.com, http://aryan.com/ will trigger the following function, hello
@app.route(
    "/hello"
)  # if the domain is aryan.com, http://aryan.com/hello will trigger the following function, hello
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        # return f'<h1>Hello, {name}!</h1> <p style="color:red;">I am excited to learn Flask.</p>'
        return render_template("index.html", username=name)
    return "Hello, world!"


# Create another route "/square/<number>", so the webapp will display the square of the number
@app.route("/square")
@app.route("/square/<number>")
def square(number=None):
    if number:
        # return str(int(number) ** 2)
        result = int(number) ** 2
        return render_template("square-result.html", number=number, result=result)
    return "No number provided."


@app.route("/weather/<city>")
def show_temp(city=None):
    temp = get_temp(city)
    return render_template("weather-result.html", city=city, temp=temp)


if __name__ == "__main__":
    app.run(debug=True)
