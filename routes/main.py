from flask import Blueprint, request
from core.response import success, error

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return success({
        "project": "SubInfo",
        "version": "0.1.0",
        "status": "running"
    })


@main.route("/health")
def health():
    return success({
        "status": "ok"
    })


@main.route("/convert")
def convert():
    url = request.args.get("url")

    if not url:
        return error(1001, "Missing parameter: url")

    return success({
        "url": url
    })
