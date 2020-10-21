import json


class OrderDataEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            print(o)
            to_serialize = {
                'items': json.dumps(o.items),
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
