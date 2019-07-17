import os
from sanic import Sanic
from sanic_json import get_json_route
from api.photo import (
    random_pohoto,
    random_photo_html,
    all_photo,
    curated_photo,
    get_photo,
    search_photo,
)

app = Sanic()
json_route = get_json_route(app)


async def index(req):
    return {"status": "healthy"}


async def routes(req):
    rv = {"urls": []}
    for handler, (rule, router) in app.router.routes_names.items():
        rv["urls"].append(rule)
    return rv


json_route("/api/photo/random", random_pohoto)
json_route("/api/photo/all", all_photo)
json_route("/api/photo/curated", curated_photo)
json_route("/api/photo/get", get_photo)
json_route("/api/photo/search", search_photo)
json_route("/random", random_photo_html)
json_route("/routers", routes)
json_route("/", index)


if __name__ == "__main__":
    debug = bool(os.getenv("DEBUG"))
    # hot reload in next release: https://github.com/channelcat/sanic/issues/168
    app.run(host="0.0.0.0", port=8000, debug=debug)
