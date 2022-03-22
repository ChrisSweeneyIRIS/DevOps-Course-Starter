from flask import Flask, render_template, request, redirect
import todo_app.data.trello_items as trello

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route("/")
def index():
    items = trello.get_items()
    return render_template("index.html", items=items)

@app.route("/add", methods=["POST"])
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

if __name__ == "__main__":
    app.run()