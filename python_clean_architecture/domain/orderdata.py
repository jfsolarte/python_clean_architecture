from python_clean_architecture.shared.domain_model import DomainModel


class OrderData(object):

    def __init__(self, items):
        self.items = items

    @classmethod
    def getdata(self):
        return [1,2,3,4,5,6,7,8]


DomainModel.register(OrderData)