
from flask import Flask, render_template, request, jsonify
from modules.shodan_lookup import shodan_host
from modules.osint_engine import domain_lookup
from modules.ai_report import generate_report

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/shodan", methods=["POST"])
def shodan():

    ip = request.json["ip"]

    data = shodan_host(ip)

    return jsonify(data)


@app.route("/domain", methods=["POST"])
def domain():

    domain = request.json["domain"]

    data = domain_lookup(domain)

    return jsonify(data)


@app.route("/report", methods=["POST"])
def report():

    data = request.json["data"]

    report = generate_report(data)

    return jsonify({"report": report})


app.run(debug=True)
