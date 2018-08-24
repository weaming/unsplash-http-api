from .unsplash_api import api


def obj_to_dict(obj):
    if not obj or isinstance(obj, (str, int, float)):
        return obj
    elif isinstance(obj, list):
        return [obj_to_dict(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: obj_to_dict(v) for k, v in obj.items()}
    else:
        return {k: obj_to_dict(v) for k, v in obj.__dict__.items()}


async def random_pohoto(req, count=10):
    res = api.photo.random(count=count)
    return {"data": obj_to_dict(res)}
