from flask import Flask, request, render_template

app = Flask(__name__)


# multiple URLs
@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return "Home Page"


# trailing slashes /
@app.route("/eziz", strict_slashes=False)
def eziz():
    return "<h2>Eziz</h2>"


# passing variables that may be empty
@app.route("/profile")
@app.route("/profile/<username>")
def profile(username=None):
    return render_template("profile.html", username = username)


# passing variables with types
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "<h3>Post ID: %d<h3>" % post_id


# allowing only listed methods
@app.route("/methods", methods=["GET", "POST"])
def methods():
    if request.method == "POST":
        return "You are using POST"
    else:
        return "You are probably using GET"


# passing objects to html templates and rendering them
@app.route("/movies")
def movies():
    movies = ["deadpool", "avengers", "hulk"]
    return render_template("movies.html", movies=movies)


if __name__ == "__main__":
    app.run()
