from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello world!</h1>"

# @app.route("/")
# def index():
#     return render_template("index.html", name="MDI")

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f"Goodbye {name}!"
    return render_template("form_post.html", name="MDI")

# @app.route("/goodbye")
# def bye():
#     return "Goodbye!"

@app.route("/goodbye")
def bye():
    name = request.args["name"]
    return f"Goodbye {name}!"
