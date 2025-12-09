# app/routes.py
"""
Flask Routes for the First-Aid KBS.

Responsibilities:
- Render input form
- Handle form submission
- Call Controller for inference
- Pass results to template
"""

from flask import Blueprint, render_template, request, current_app

ui_blueprint = Blueprint("ui", __name__)


@ui_blueprint.route("/", methods=["GET"])
def index():
    """
    Render the main input form.
    """
    return render_template("index.html")


@ui_blueprint.route("/diagnose", methods=["POST"])
def diagnose():
    """
    Handle form submission, call controller, and render results.
    """
    user_input = request.form.get("symptom", "")

    controller = current_app.config["CONTROLLER"]
    result = controller.diagnose(user_input)

    return render_template(
        "index.html",
        result=result
    )
