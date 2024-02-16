import json


def convert_rate_obj_to_json(obj):
    return json.dumps({
        'charcode': obj.charcode,
        'date': str(obj.date),
        'rate': obj.rate
    })
