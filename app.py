from flask import Flask, jsonify
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    return jsonify({
        "project": "SubInfo",
        "version": app.config["VERSION"],
        "status": "running"
    })


if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
