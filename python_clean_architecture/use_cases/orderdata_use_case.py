from python_clean_architecture.shared import use_case as uc
from python_clean_architecture.shared import response_object as res

class OrderDataGetUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_object):

        #if not request_object:
            #return res.ResponseFailure.build_from_invalid_request_object(request_object)

        storage_rooms = self.repo.order(items=request_object.items)
        return res.ResponseSuccess(storage_rooms)
 