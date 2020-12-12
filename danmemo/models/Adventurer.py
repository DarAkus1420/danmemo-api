from . import db
from mongoengine import EmbeddedDocumentField, Document
from .Info import Info

class Adventurer(Document):
    info = EmbeddedDocumentField(Info, required=True)

    # @classmethod
    # def new(cls, info):
        # return Adventurer(info)
    
    
    def __str__(self):
        return self.name
    

