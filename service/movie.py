from service import root_dir, nice_json
from flask import Flask
from werkzeug.exceptions import NotFound
import json


app = Flask(__name__)

with open("{}/database/movie.json".format(root_dir()), "r") as f:
    movie = json.load(f)


@app.route("/", methods=['GET'])
def hello():
    return nice_json({
        "uri": "/",
        "subresource_uris": {
            "movies": "/movie",
            "movie": "/movies/<id>"
        }
    })

@app.route("/movie/<movieid>", methods=['GET'])
def movie_info(movieid):
    if movieid not in movie:
        raise NotFound

    result = movie[movieid]
    result["uri"] = "/movies/{}".format(movieid)

    return nice_json(result)


@app.route("/movie", methods=['GET'])
def movie_record():
    return nice_json(movie)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
