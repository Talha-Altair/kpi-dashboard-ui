from flask import Flask, render_template, request, url_for, redirect, session
from settings import HOST, PORT, BACKEND_URL

import json

f1, f2, f3, f4 = open("./json/academics.json", "r"), open("./json/home.json", "r"), open("./json/research.json", "r"), open("./json/contributions.json", "r")
academics_data = json.load(f1)
home_data = json.load(f2)
research_data = json.load(f3)
contributions_data = json.load(f4)


app = Flask(__name__)


@app.route("/")
def login():
    return redirect("/dashboard/{}".format("balaji"))


@app.route("/dashboard/<string:username>")
def index(username):
    return render_template("index.html", data=home_data, active="dashboard")


@app.route("/dashboard/<string:username>/academics")
def academic(username):

    best_pass_class = academics_data['charts']['pass_percentage_data']
    best_matr_class = academics_data['charts']['material_quality_data']
    best_ques_class = academics_data['charts']['ques_quality_data']['base_data']

    best_pass_class = sorted(best_pass_class, key=lambda x: x[1], reverse=True)
    best_matr_class = sorted(best_matr_class, key=lambda x: x[1], reverse=True)
    best_ques_class = sorted(best_ques_class, key=lambda x: x['y'], reverse=True)

    best_pass_class = best_pass_class[0][0]
    best_matr_class = best_matr_class[0][0]
    best_ques_class = best_ques_class[0]['name']

    academics_data['best_pass_class'] = best_pass_class
    academics_data['best_matr_class'] = best_matr_class
    academics_data['best_ques_class'] = best_ques_class

    return render_template(
        "academics.html",
        data=academics_data,
        json_data=json.dumps(academics_data),
        active="academics",
    )

@app.route("/dashboard/<string:username>/research")
def research(username):
    return render_template(
        "research.html",
        data=research_data,
        json_data=json.dumps(research_data),
        active="research",
    )

@app.route("/dashboard/<string:username>/contributions")
def contributions(username):
    return render_template(
        "contributions.html",
        data=contributions_data,
        json_data=json.dumps(contributions_data),
        active="contributions",
    )


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
