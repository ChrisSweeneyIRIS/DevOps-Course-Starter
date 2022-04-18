from flask import Flask, render_template, request, redirect
import todo_app.data.trello_items as trello
from view_model import view_model

from todo_app.flask_config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route("/")
    def index():
        items = trello.get_items()
        item_view_model = view_model(items)
        return render_template("index.html", view_model = item_view_model)

    @app.route("/add", methods = ["POST"])
    def add():
        trello.add_item(request.form.get("title"), request.form.get("description"))
        return redirect("/")

    @app.route("/complete/<id>")
    def complete(id: str):
        trello.complete_item(id)
        return redirect("/")

    @app.route("/progress/<id>")
    def progress(id: str):
        trello.progress_item(id)
        return redirect("/")

    @app.route("/remove/<id>")
    def remove(id):
        trello.remove_item(id)
        return redirect("/")

    return app