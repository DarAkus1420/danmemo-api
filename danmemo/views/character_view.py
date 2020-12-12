from flask import request
from flask import Blueprint
from ..models.Adventurer import Adventurer
from ..models.Info import Info
from ..responses import resp

api_v2 = Blueprint('api', __name__, url_prefix='/api/v2')

@api_v2.route('/tasks', methods=['GET'])
def hello():
    new_info = Info(
        name='Lyd',
        character='Lyd',
        category='adventurer',
        rarity=4,
        unit_type='p damage',
        skill_element='earth',
        hero_ascension=True,
        method_obtained='regular'
    )
    adventurer = Adventurer(info=new_info)
    print(adventurer.save())
    return resp(adventurer)
