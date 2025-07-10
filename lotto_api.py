from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/lotto-data")
def lotto_data():
    url = "https://www.nationallottery.co.za/index.php?task=results.redirectPageURL&Itemid=265&option=com_weaver&controller=lotto-history"
    payload = {
        "gameName": "LOTTO",
        "drawNumber": "",
        "isAjax": "true"
    }
    resp = requests.post(url, data=payload)
    data = resp.json().get("data", {}).get("drawDetails", {})

    draws = [{
        "date": data.get("drawDate"),
        "numbers": [
            data.get("ball1"), data.get("ball2"),
            data.get("ball3"), data.get("ball4"),
            data.get("ball5"), data.get("ball6")
        ]
    }]
    return jsonify(draws)

if name == "__main__":
    app.run(host="0.0.0.0", port=8000)
