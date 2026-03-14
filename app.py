from flask import Flask,render_template,request,jsonify
from modules.sherlock_search import search_username
from modules.threat_feed import get_threats
from modules.ai_osint import ask_ai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/username",methods=["POST"])
def username():

    username = request.json["username"]

    data = search_username(username)

    return jsonify({"result":data})


@app.route("/ai",methods=["POST"])
def ai():

    question = request.json["question"]

    data = ask_ai(question)

    return jsonify(data)


@app.route("/threats")
def threats():

    data = get_threats()

    return jsonify(data)


app.run(debug=True)
