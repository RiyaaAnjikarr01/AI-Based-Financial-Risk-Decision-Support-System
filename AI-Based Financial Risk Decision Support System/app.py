from flask import Flask, render_template, request
from services.risk_service import RiskService
from services.simulation_service import SimulationService

app = Flask(__name__)

risk_service = RiskService()

@app.route("/")
def home():

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


@app.route("/predict", methods=["POST"])
def predict():

    income = float(request.form["income"])
    debt = float(request.form["debt"])
    credit = float(request.form["credit"])

    risk = risk_service.get_risk(income, debt, credit)

    return render_template(
        "prediction.html",
        risk=risk,
        income=income,
        debt=debt,
        credit=credit
    )


@app.route("/simulation", methods=["POST"])
def simulation():

    income = float(request.form["income"])
    debt = float(request.form["debt"])

    scenarios = SimulationService.generate_scenarios(income, debt)

    return render_template("simulation.html", scenarios=scenarios)


if __name__ == "__main__":
    app.run(debug=True)