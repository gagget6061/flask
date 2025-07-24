from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def index():
    return send_from_directory('templates',"index.html")

@app.route('/<path:name>')
def start(name):
    return send_from_directory('templates',name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)