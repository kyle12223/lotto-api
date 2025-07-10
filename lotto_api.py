from flask import Flask, jsonify

app = Flask(__name__)

# Your manually added old Lotto data
lotto_data = [
    {
        "date": "2025-07-06",
        "numbers": [5, 12, 23, 34, 41, 47]
    },
    {
        "date": "2025-07-03",
        "numbers": [9, 15, 27, 33, 38, 44]
    },
    {
        "date": "2025-06-30",
        "numbers": [2, 14, 18, 21, 36, 49]
    }
]

@app.route("/lotto-data", methods=["GET"])
def get_lotto_data():
    return jsonify(lotto_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
