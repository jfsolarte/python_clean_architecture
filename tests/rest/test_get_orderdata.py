import json
from unittest import mock
import requests
from python_clean_architecture.domain.orderdata import OrderData
from python_clean_architecture.shared import response_object as res

storageroom1_dict = [1, 2, 3, 4, 5, 6, 7, 8]

storageroom1_domain_model = OrderData.getdata()

storagerooms = [storageroom1_domain_model]


@mock.patch('python_clean_architecture.use_cases.orderdata_use_case.OrderDataGetUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseSuccess(storagerooms)

    http_response = client.post('/orderdata',json={"items":[1, 2, [3, 4, [5, 6], 7], 8]})

    assert json.loads(http_response.data.decode('UTF-8')) == [storageroom1_dict]
    assert http_response.status_code == 200
    assert http_response.mimetype == 'application/json'