from flask import Flask, render_template, request, redirect, url_for
from todo_app.data import session_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = session_items.get_items()
    return render_template("index.html", items = items)

@app.route('/items/new', methods=['POST'])
def add_item():
    title = request.form['title']
    session_items.add_item(title)
    return redirect(url_for('index'))
