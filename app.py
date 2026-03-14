from flask import Flask, render_template, request, jsonify

from modules.username_scan import scan_username
from modules.shodan_lookup import shodan_search
from modules.osint_engine import domain_lookup
from modules.graph_builder import build_graph
from modules.attack_map import get_attack_points
from modules.ai_report import generate_report

app = Flask(__name__)


# Dashboard page
@app.route("/")
def home():
    return render_template("dashboard.html")


# Username OSINT (Sherlock)
@app.route("/username", methods=["POST"])
def username():

    username = request.json["username"]

    result = scan_username(username)

    return jsonify(result)


# Shodan intelligence lookup
@app.route("/shodan", methods=["POST"])
def shodan():

    ip = request.json["ip"]

    result = shodan_search(ip)

    return jsonify(result)


# Domain OSINT
@app.route("/domain", methods=["POST"])
def domain():

    domain = request.json["domain"]

    result = domain_lookup(domain)

    return jsonify(result)


# Investigation graph
@app.route("/graph", methods=["POST"])
def graph():

    target = request.json["target"]

    graph_data = build_graph(target)

    return jsonify(graph_data)


# Global cyber attack map
@app.route("/attacks")
def attacks():

    attack_points = get_attack_points()

    return jsonify(attack_points)


# AI OSINT report generator
@app.route("/report", methods=["POST"])
def report():

    data = request.json["data"]

    report = generate_report(data)

    return jsonify({"report": report})


# Run server
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
