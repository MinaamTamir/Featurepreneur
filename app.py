from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return "Enter something with the url"
@app.route('/<path:path>')
def default(path):
    return path


if __name__ == "__main__":
    app.run(debug=True)