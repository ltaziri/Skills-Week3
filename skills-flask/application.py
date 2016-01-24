from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def app_form_page():
    """Show a career form page."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def app_response():
    """Show an application-response page."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    position = request.form.get("position")

    return render_template("application-response.html",
                                first_name=first_name,
                                last_name=last_name,
                                salary=salary,
                                position=position)

    
   
if __name__ == "__main__":
    app.run(debug=True)
