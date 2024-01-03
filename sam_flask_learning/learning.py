from flask import Flask
app = Flask(__name__)


# @app.route("/")
# @app.route("/home")
# def home():
#     return "<h1>Home Page</h1>"
#
#
# @app.route("/about")
# def about():
#     return "<h1>About Page</h1>"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask , render_template
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return render_template('index.html')
#
# @app.route("/about")
# @app.route("/about/info")
# def about():
#     return render_template('about.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
from flask import Flask, render_template, url_for
# app = Flask(__name__)
#
# posts = [
#     {
#         'author': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }
# ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

