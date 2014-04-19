

def write(battlename = None, battlenumber = None):
    if (type(battlename) != str ) or (type(battlenumber) != str):
        return "Bad Arguments"
    elif len(battlenumber) != 4:
        return 'invalid battlenumber length'
    
    
