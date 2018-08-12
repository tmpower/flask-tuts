from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# Config
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "myblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# init MySQL
mysql = MySQL(app)

Articles = Articles()

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def articles():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()
    cur.close()

    if result > 0:
        return render_template("articles.html", articles = articles)
    else:
        msg = "No Articles Yet"
        return render_template("articles.html", msg = msg)


@app.route("/article/<string:id>/")
def article(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()
    cur.close()

    return render_template("article.html", article = article)


class RegisterForm(Form):
    name = StringField("Name", [validators.Length(min=1, max=50)])
    username = StringField("Username", [validators.Length(min=4, max=25)])
    email = StringField("Email", [validators.Length(min=6, max=50)])
    password = PasswordField("Password", [
        validators.DataRequired(),
        validators.EqualTo("confirm", message="Passwords don't match")
    ])
    confirm = PasswordField("Confirm Password")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        mysql.connection.commit()
        cur.close()

        flash("Registered, login!", "success")

        return redirect( url_for("login") )

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password_candidate = request.form["password"]

        cur = mysql.connection.cursor()

        result = cur.execute("SELECT * FROM users WHERE username=%s", [username])

        if result > 0:
            data = cur.fetchone()
            cur.close()
            password = data["password"]

            if sha256_crypt.verify(password_candidate, password):
                session["logged_in"] = True
                session["username"] = username

                flash("Now you are logged in", "success")
                return redirect( url_for("dashboard") )

            else:
                error = "Invalid password"
                return render_template("login.html", error = error)
        else:
            error = "Invalid username"
            return render_template("login.html", error = error)

    return render_template("login.html")


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first', "danger")
            return redirect(url_for('login'))
    return wrap


@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("You are logged out", "success")
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles")

    articles = cur.fetchall()
    cur.close()

    if result > 0:
        return render_template("dashboard.html", articles = articles)
    else:
        msg = "No Articles Yet"
        return render_template("dashboard.html", msg = msg)


class ArticleForm(Form):
    title = StringField("Title", [validators.Length(min=1, max=250)])
    body = TextAreaField("Body", [validators.Length(min=30)])


@app.route("/add_article", methods=["GET", "POST"])
@login_required
def add_article():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        body = form.body.data

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)", (title, body, session["username"]))

        mysql.connection.commit()
        cur.close()

        flash("Article created", "success")
        return redirect(url_for("dashboard"))

    return render_template("add_article.html", form = form)


@app.route("/edit_article/<string:id>", methods=["GET", "POST"])
@login_required
def edit_article(id):

    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])

    article = cur.fetchone()

    form = ArticleForm(request.form)

    form.title.data = article["title"]
    form.body.data = article["body"]

    if request.method == "POST" and form.validate():
        title = request.form["title"]
        body = request.form["body"]

        cur = mysql.connection.cursor()
        cur.execute("UPDATE articles SET title=%s, body=%s WHERE id=%s ", [title, body, id])

        mysql.connection.commit()
        cur.close()

        flash("Article updated", "success")
        return redirect(url_for("dashboard"))

    return render_template("edit_article.html", form = form)


@app.route("/delete_article/<string:id>", methods=["POST"])
@login_required
def delete_article(id):

    cur = mysql.connection.cursor()
    cur.execute("DELETE * FROM articles WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()

    flash("Article deleted", "success")
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.secret_key = "secret123"
    app.run(debug=True)
