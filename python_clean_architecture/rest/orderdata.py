import json
from flask import Blueprint, request, Response
import sys
from python_clean_architecture.use_cases import request_objects as req
from python_clean_architecture.repository import memrepo as mr
from python_clean_architecture.use_cases import orderdata_use_case as uc
from python_clean_architecture.serializers import orderdata_serializer as ser

blueprint = Blueprint('storageroom', __name__)


@blueprint.route('/orderdata', methods=['POST'])
def orderdata():

    
    data = request.json
    #print('-------------->', file=sys.stderr)
    #print(data); 
    #return json.dumps(data['items'])
    request_object = req.OrderDataGetRequestObject.from_dict(data)
    
    repo = mr.MemRepo(data)
    use_case = uc.OrderDataGetUseCase(repo)

    response = use_case.execute(request_object)

    return Response(json.dumps(response.value, cls=ser.OrderDataEncoder),
                    mimetype='application/json',
                    status=200)