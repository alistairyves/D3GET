import json
class NameWriter:
    def __init__(self):
        self.data=[]
    def write(self, battlename = None, battlenumber = None):
        if len(str(battlenumber)) != 4:
            return 'invalid battlenumber length'
    
    
