def obj_to_dict(obj):
    if not obj or isinstance(obj, (str, int, float)):
        return obj
    elif isinstance(obj, list):
        return [obj_to_dict(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: obj_to_dict(v) for k, v in obj.items() if str(k)[0] != '_'}
    else:
        return {
            k: obj_to_dict(v)
            for k, v in obj.__dict__.items() if str(k)[0] != '_'
        }
