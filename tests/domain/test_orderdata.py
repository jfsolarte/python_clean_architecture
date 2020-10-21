import uuid
from python_clean_architecture.domain.orderdata import OrderData


def test_orderdata_model_init():
    
    items=[1, 2, [3, 4, [5, 6], 7], 8]
    orderdata = OrderData(items)
    assert orderdata.items == [1, 2, [3, 4, [5, 6], 7], 8]


def test_orderdata_result():
    
    orderdata = OrderData(items=[1, 2, [3, 4, [5, 6], 7], 8])
    data = orderdata.getdata(); 
    
    assert data[0] == 1
    assert data[1] == 2
    assert data[2] == 3
    assert data[3] == 4
    assert data[4] == 5
    assert data[5] == 6
    assert data[6] == 7
    assert data[7] == 8