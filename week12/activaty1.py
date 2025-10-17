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

# activity 1.3
# Add a new route that takes an integer parameter and returns its square
# user should input an integer in the URL like /cal/4 and the output should be "The square of 4 is 16"
@app.route('/cal/<int:number>')
def show_square(number):
    return f"The square of {number} is {number**2}"
 