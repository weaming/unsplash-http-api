from sanic import Sanic
from sanic_json import get_json_route, add_route
from api.photo import (
    random_pohoto,
    random_photo_html,
    all_photo,
    curated_photo,
    get_photo,
)

app = Sanic()
json_route = get_json_route(app)


async def index(req):
    return response.redirect("/random")


json_route("/api/random", random_pohoto)
json_route("/api/all", all_photo)
json_route("/api/curated", curated_photo)
json_route("/api/get", get_photo)
json_route("/random", random_photo_html)
json_route("/", index)


if __name__ == "__main__":
    import os

    debug = True if os.getenv("DEBUG") else False
    # hot reload in next release: https://github.com/channelcat/sanic/issues/168
    app.run(host="0.0.0.0", port=8000, debug=debug)
