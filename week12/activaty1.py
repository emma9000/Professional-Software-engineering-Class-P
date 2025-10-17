from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/username/<name>")
def learn_flask(name):
    return f"{name} is learning Flask!"
#if __name__ == "__main__":
#    app.run(debug=True)