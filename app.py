from flask import Flask, render_template, request
from settings import HOST, PORT, BACKEND_URL

app = Flask(__name__)

@app.route("/dashboard/<string:username>")
def index(username):

    data = {
        'basic': {
            'name': 'Dr. Balaji Ramanujam',
            'designation': 'Professor',
            'email': 'balaji.cse@crescent.education',
            'doj': '21-09-2017',
            'exp': '12 Years',
            'research': [
                'Data Mining',
                'Machine Learning',
                'Big Data Analytics',
                'Cloud Computing'
            ]
        }
    }

    return render_template("index.html", data = data)


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
