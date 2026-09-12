from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Flask App is running inside Docker 🚀"

@app.route("/about")
def about():
    return "This is my Flask Docker Project."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)