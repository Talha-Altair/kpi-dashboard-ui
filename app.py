from flask import Flask, render_template, request, url_for, redirect, session
from settings import HOST, PORT, BACKEND_URL

import json

app = Flask(__name__)

@app.route("/")
def login():

    return redirect('/dashboard/{}'.format('balaji'))


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
            ],
            "ques_quality_data": {
                "base_data": [
                    {"name": "compiler", "y": 52.74, "drilldown": "compiler"},
                    {"name": "Green Design", "y": 72.74, "drilldown": "Green Design"},
                    {
                        "name": "Operating System",
                        "y": 62.74,
                        "drilldown": "Operating System",
                    },
                    {
                        "name": "Cloud Computing",
                        "y": 82.74,
                        "drilldown": "Cloud Computing",
                    },
                ],
                "drilldown_data": [
                    {
                        "name": "compiler",
                        "id": "compiler",
                        "data": [["cat1", 47], ["cat2", 50], ["endsem", 75]],
                    },
                    {
                        "name": "Green Design",
                        "id": "Green Design",
                        "data": [["cat1", 87], ["cat2", 90], ["endsem", 85]],
                    },
                    {
                        "name": "Operating System",
                        "id": "Operating System",
                        "data": [["cat1", 87], ["cat2", 90], ["endsem", 85]],
                    },
                    {
                        "name": "Cloud Computing",
                        "id": "Cloud Computing",
                        "data": [["cat1", 87], ["cat2", 90], ["endsem", 85]],
                    },
                ],
            },
            "material_quality_data": [
                ["Compiler", 66],
                ["Green Design", 18],
                ["Operating System", 98],
                ["Cloud Computing", 69],
            ],
        },
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
            "teaching_methods": [
                "Slow Paced Lectures",
                "Focus onCase Study",
                "Frequent Group Discussion",
                "Real time Problem Solving",
            ],
        },
    }

    return render_template(
        "academics.html", data=data, json_data=json.dumps(data), active="academics"
    )


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
