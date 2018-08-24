from sanic import response
from .unsplash_api import api
from .to_json import obj_to_dict



async def random_pohoto(req, count=10):
    res = api.photo.random(count=count)
    return {"data": obj_to_dict(res)}


async def random_photo_html(req):
    res = obj_to_dict(api.photo.random(count=1))[0]
    url = res["urls"]["raw"]
    try:
        location = res["location"]
        if isinstance(location, dict):
            location = location["title"]
    except KeyError as e:
        print(e)
        print(res)
        location = "unknown location"

    html = (
        '<body style="margin: 0; display: inline-block;">'
        '<img src="{url}" alt="{location}" title="{location}" '
        'style="max-width: 100vw; max-height: 100vh; margin: 0 auto;">'
        "</body>"
    )
    return response.html(html.format(url=url, location=location))


async def index(req):
    return response.redirect("/random")
