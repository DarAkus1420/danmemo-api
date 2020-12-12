from mongoengine import StringField, IntField, BooleanField, EmbeddedDocument

CATEGORIES = [
    'adventurer',
    'assist'
]

UNIT_TYPES = [
    'p damage'
]

SKILL_ELEMENTS = [
    'earth'   
]

METHODS_OBTAINED = [
    'regular',
    'time-limited'
]

class Info(EmbeddedDocument):
    
    name = StringField(max_length=150, required=True)
    character = StringField(max_length=100, required=True)
    category = StringField(required=True, choices=CATEGORIES)
    rarity = IntField(min_value=1, max_value=4, required=True)
    unit_type = StringField(required=True, choices=UNIT_TYPES)
    skill_element = StringField(required=True, choices=SKILL_ELEMENTS)
    hero_ascension = BooleanField(required=True)
    method_obtained = StringField(required=True, choices=METHODS_OBTAINED)


