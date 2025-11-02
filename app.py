from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Demo project using Flask and deployment on Render and Railway platforms. And also on - Github Tunelling"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)