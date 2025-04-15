from flask import Flask, render_template, request, redirect
from weather import get_temp

app = Flask(__name__)


"""
Homepage
"""


# If the domain is aryan.com, https://aryan.com/ will trigger the following function, hello
@app.route("/")
def index():
    """"""
    return "This is the hompage."


"""
hello route
"""


# If the domain is aryan.com, https://aryan.com/hello will trigger the following function, hello
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    if name:
        # return f'<h1>Hello, {name}!</h1> <p style="color:red;">I am excited to learn Flask.</p>'
        return render_template("index.html", username=name)
    return "Hello, world!"


"""
Another route example
"""


# Create another route "/square/<number>", so the webapp will display the square of the number
@app.route("/square")
@app.route("/square/<number>")
def square(number=None):
    if number:
        # return str(int(number) ** 2)
        result = int(number) ** 2
        return render_template("square-result.html", number=number, result=result)
    return "No number provided."


"""
404
"""


@app.errorhandler(404)
def page_not_found(e):
    """return a custom 404 error page"""
    # return 'No page found! 😔'
    return render_template("404.html")


"""
Weather API, Weather API + form (get & post)
"""


@app.route("/weather/<city>")
def show_temp(city=None):
    temp = get_temp(city)
    return render_template("weather-result.html", city=city.title(), temp=temp)


@app.get("/weather")
def get_weather():
    """Display the form for user to input a city name"""
    return render_template("weather-form.html")


@app.post("/weather")
def post_weather():
    """
    Display the result after submitting the form
    """
    city_name = request.form["city"]
    temp = get_temp(city_name)
    return render_template("weather-result.html", city=city_name.title(), temp=temp)


"""
Student registration example
"""
COURSES = ['Excel', 'Web', 'Tax']
registration = {}  # {'Aryan': 'Web', 'Sol': 'Tax'}


@app.get("/register/")
def show_register_form():
    return render_template("register-form.html", courses=COURSES)


@app.post("/register/")
def register_course():
    """"""
    name = request.form.get("fullname")
    course = request.form.get("course")
    # some validation
    if course not in COURSES:
        return f'Get out of here, hacker {name}!'
    registration[name] = course
    # return "Successfully registered!"
    return redirect("/enrollments")


@app.route("/enrollments")
def show_enrollments():
    return render_template("enrollments.html", students=registration)


if __name__ == "__main__":
    app.run(debug=True)
