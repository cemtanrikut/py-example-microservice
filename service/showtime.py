from service import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("{}/database/showtime.json".format(root_dir()), "r") as f:
    showtime = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "showtimes": "/showtime",
            "showtime": "/showtime/<date>"
        }
    })


@app.route("/showtime", methods=['GET'])
def showtime_list():
    return nice_json(showtime)


@app.route("/showtime/<date>", methods=['GET'])
def showtime_record(date):
    if date not in showtime:
        raise NotFound
    return nice_json(showtime[date])

if __name__ == "__main__":
    app.run(port=5002, debug=True)