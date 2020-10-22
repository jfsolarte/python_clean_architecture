from python_clean_architecture.domain import orderdata as sr
import sys

class MemRepo:

    def __init__(self, entries=None):
        print(entries)
        print('ssssssssssssssssssss')
        self._entries = []
        if entries:
            self._entries.extend(entries)


    def order(self, items=None):
        listOrder = []
        self.extractor(items,listOrder)
       
        return {'result':listOrder}

    def extractor(self,items, listOrder):
        
        for x in items:
            if isinstance(x, list):
                self.extractor(x,listOrder)
            else:    
                listOrder.append(x)