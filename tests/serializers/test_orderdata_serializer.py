import datetime
import json
import uuid

import pytest

from python_clean_architecture.serializers import orderdata_serializer as srs
from python_clean_architecture.domain.orderdata import OrderData


def test_serialize_domain_orderdata():
    code = uuid.uuid4()

    room = OrderData(
        items=[1, 2, [3, 4, [5, 6], 7], 8]
    )

    expected_json = '{"items": "[1, 2, [3, 4, [5, 6], 7], 8]"}'

    json_orderdata = json.dumps(room, cls=srs.OrderDataEncoder)
    
    print(expected_json); 
    print(json_orderdata); 

    assert json.loads(json_orderdata) == json.loads(expected_json)
