from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to My Python Website!</h1> <hr>"

if __name__ == "__main__":
    app.run(debug=True)