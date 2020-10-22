
import collections
import sys
from python_clean_architecture.shared import request_object as req

class OrderDataGetRequestObject(req.ValidRequestObject):


    def __init__(self, items=None):
        self.items = items

    @classmethod
    def from_dict(cls, adict):
        print(adict); 
        return OrderDataGetRequestObject(items=adict['items'])

    def __nonzero__(self):
        return True