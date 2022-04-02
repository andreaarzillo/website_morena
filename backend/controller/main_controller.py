from flask import jsonify, flash, request, render_template, Blueprint, Response
from werkzeug.utils import secure_filename

main_controller = Blueprint("patient_controller", __name__)


@main_controller.post("/")
def upload_file():
    return jsonify("ciao")


@main_controller.get("/")
def index():
    return render_template("index.html")
