import uuid
import json
import pytest
from unittest import mock

from python_clean_architecture.domain.orderdata import OrderData
from python_clean_architecture.use_cases import request_objects as ro
from python_clean_architecture.use_cases import orderdata_use_case as uc



@pytest.fixture
def domain_orderdata():
    return [1, 2, [3, 4, [5, 6], 7], 8]


def test_storageroom_list_without_parameters(domain_orderdata):
    repo = mock.Mock()
    repo.items = domain_orderdata

    orderdata_get_use_case = uc.OrderDataGetUseCase(repo)
    request_object = ro.OrderDataGetRequestObject.from_dict(json.loads('{"items":[1, 2, [3, 4, [5, 6], 7], 8]}'))

    response_object = orderdata_get_use_case.execute(request_object)

    assert bool(response_object) is True

    #repo.list.assert_called_with()
    assert response_object.value != domain_orderdata