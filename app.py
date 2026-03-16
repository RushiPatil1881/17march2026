from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Helloooooo from Docker container running Python Flask!"

@app.route("/health")
def health():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
