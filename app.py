from flask import Flask, render_template, request
from settings import HOST, PORT, BACKEND_URL

import json

app = Flask(__name__)


@app.route("/dashboard/<string:username>")
def index(username):
    data = {
        "username": username,
        "basic": {
            "name": "Dr. Balaji Ramanujam",
            "designation": "Professor",
            "email": "balaji.cse@crescent.education",
            "doj": "21-09-2017",
            "exp": "12 Years",
            "research": [
                "Data Mining",
                "Machine Learning",
                "Big Data Analytics",
                "Cloud Computing",
            ],
        },
    }

    return render_template("index.html", data=data, active="dashboard")


@app.route("/dashboard/<string:username>/academics")
def academic(username):
    data = {
        "username": username,
        "charts": {
            "pass_percentage_data": [
                ["Compiler", 56],
                ["Green Design", 78],
                ["Operating System", 94],
                ["Cloud Computing", 69],
            ]
        },
    }

    return render_template("academics.html", data=data, json_data = json.dumps(data), active="academics")


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
