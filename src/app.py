from flask import Flask, render_template

app = Flask(__name__)

app.template_folder = "templates"
app.static_folder = "static"


@app.route('/', methods=["POST","GET"])
def index():
    return render_template("index.html", methods="[GET]")


def start_server(host='0.0.0.0', port=8000):
    return app.run(debug=True, host=host, port=port)

if(__name__ == "__main__"):
    start_server()