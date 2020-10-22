from python_clean_architecture.use_cases import request_objects as ro

import json
def test_build_orderdata_get_request_object_without_parameters():
    req = ro.OrderDataGetRequestObject()

    assert bool(req) is True


def test_build_file_get_request_object_from_empty_dict():
    req = ro.OrderDataGetRequestObject.from_dict(json.loads('{"items":[1, 2, [3, 4, [5, 6], 7], 8]}'))

    assert bool(req) is True