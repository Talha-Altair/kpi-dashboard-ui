from flask import Flask, render_template, request, url_for, redirect, session
import requests
from settings import HOST, PORT, BACKEND_URL
from utils import get_dashboard_data
import json

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/redirect", methods=["GET", "POST"])
def redirect_to_dashboard():
    data = dict(request.form)

    res = requests.get(f"{BACKEND_URL}/login", json=data)

    if res.status_code == 200:
        return redirect("/dashboard/{}".format(data["username"]))

    return "Invalid Credentials"


@app.route("/dashboard/<string:username>")
def index(username):
    data = get_dashboard_data(username)

    return render_template(
        "index.html", data=data, json_data=json.dumps(data), active="dashboard"
    )


@app.route("/dashboard/<string:username>/academics")
def academic(username):
    data = get_dashboard_data(username)

    best_pass_class = data["charts"]["pass_percentage_data"]
    best_matr_class = data["charts"]["material_quality_data"]
    best_ques_class = data["charts"]["ques_quality_data"]["base_data"]

    best_pass_class = sorted(best_pass_class, key=lambda x: x[1], reverse=True)
    best_matr_class = sorted(best_matr_class, key=lambda x: x[1], reverse=True)
    best_ques_class = sorted(best_ques_class, key=lambda x: x["y"], reverse=True)

    best_pass_class = best_pass_class[0][0]
    best_matr_class = best_matr_class[0][0]
    best_ques_class = best_ques_class[0]["name"]

    data["best_pass_class"] = best_pass_class
    data["best_matr_class"] = best_matr_class
    data["best_ques_class"] = best_ques_class

    return render_template(
        "academics.html",
        data=data,
        json_data=json.dumps(data),
        active="academics",
    )


@app.route("/dashboard/<string:username>/research")
def research(username):
    data = get_dashboard_data(username)

    return render_template(
        "research.html",
        data=data,
        json_data=json.dumps(data),
        active="research",
    )


@app.route("/dashboard/<string:username>/contributions")
def contributions(username):
    data = get_dashboard_data(username)

    return render_template(
        "contributions.html",
        data=data,
        json_data=json.dumps(data),
        active="contributions",
    )


@app.route("/dashboard/<string:username>/networking")
def networking(username):
    data = get_dashboard_data(username)

    return render_template(
        "networking.html",
        data=data,
        json_data=json.dumps(data),
        active="networking",
    )


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
