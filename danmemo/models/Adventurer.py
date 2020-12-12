from . import db

class Adventurer(db.Document):
    name = db.StringField(required=True)
    
    @classmethod
    def new(cls, name):
        return Adventurer(name=name)
    
        
    def delete(self):
        try:
            self.delete()
            return True
        except:
            return False
    
    def __str__(self):
        return self.name
    

