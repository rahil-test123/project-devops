from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "DevOps API is running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "OK"
    })

@app.route("/info")
def info():
    return jsonify({
        "project": "DevOps Cloud Project",
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)