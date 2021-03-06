import logging

from sanic import response
from .unsplash_api import api
from .to_json import obj_to_dict
from .helpers import http_get

allowed_order_type = ["latest", "oldest", "popular"]


async def random_pohoto(req, count=10, username=None, query=None):
    """
    :param count: The number of photos to return. (Default: 1; max: 30)
    """
    res = api.photo.random(count=count, username=username, query=query)
    return {"data": obj_to_dict(res)}


async def random_photo_html(req, webp=False):
    res = obj_to_dict(api.photo.random(count=1))[0]
    if webp:
        url = res["urls"]["regular"]

        # webp
        binary = await http_get(url.replace("fm=jpg", "fm=webp"))
        return response.raw(binary, content_type="image/webp")

    url = res["urls"]["raw"]
    try:
        location = res["location"]
        if isinstance(location, dict):
            location = location["title"]
    except KeyError as e:
        logging.warning(str(e))
        logging.warning(res)
        location = "unknown location"

    html = (
        '<body style="margin: 0; display: inline-block;">'
        '<img src="{url}" alt="{location}" title="{location}" '
        'style="max-width: 100vw; max-height: 100vh; margin: 0 auto;">'
        "</body>"
    )
    return response.html(html.format(url=url, location=location))


async def all_photo(req, page=1, per_page=10, order_by="latest"):
    if order_by not in allowed_order_type:
        return {"reason": "allowed order_by values {}".format(allowed_order_type)}, 400

    res = api.photo.all(page=page, per_page=per_page, order_by=order_by)
    return {"data": obj_to_dict(res)}


async def curated_photo(req, page=1, per_page=10, order_by="latest"):
    if order_by not in allowed_order_type:
        return {"reason": "allowed order_by values {}".format(allowed_order_type)}, 400

    res = api.photo.curated(page=page, per_page=per_page, order_by=order_by)
    return {"data": obj_to_dict(res)}


async def get_photo(req, id):
    res = api.photo.get(id)
    return {"data": obj_to_dict(res)}


async def search_photo(req, query, page=1, per_page=10):
    res = api.search.photos(query, page=page, per_page=per_page)
    return {"data": obj_to_dict(res)}
