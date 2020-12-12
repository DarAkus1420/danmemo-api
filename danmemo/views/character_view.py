from flask import request
from flask import Blueprint
from ..models.Adventurer import Adventurer
from ..responses import resp

api_v2 = Blueprint('api', __name__, url_prefix='/api/v2')

@api_v2.route('/tasks', methods=['GET'])
def hello():
    adventurer = Adventurer.new('Nuevo')
    print(adventurer.save())
    return resp(adventurer.name)
