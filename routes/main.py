from flask import Blueprint, jsonify

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return jsonify({
        "project": "SubInfo",
        "version": "0.1.0",
        "status": "running"
    })


@main.route("/health")
def health():
    return jsonify({
        "status": "ok"
    })
