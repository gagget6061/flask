from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./index.html')

@app.route("/products")
def index():
    return render_template('./products.html')

#@app.route("/")
#def index():
 #   return send_from_directory('html2',"index.html")

#@app.route('/<path:name>')
#def start(name):
#    return send_from_directory('html2',name)

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", debug=True, port=5000)