from flask import Flask, render_template, request
from settings import HOST, PORT, BACKEND_URL

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
