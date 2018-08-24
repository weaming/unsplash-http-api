from sanic import Sanic
from sanic_json import get_json_route
from api.random import random_pohoto

app = Sanic()
json_route = get_json_route(app)

json_route("/api/random", random_pohoto)


if __name__ == "__main__":
    import os

    debug = True if os.getenv("DEBUG") else False
    # hot reload in next release: https://github.com/channelcat/sanic/issues/168
    app.run(host="0.0.0.0", port=8000, debug=debug)
