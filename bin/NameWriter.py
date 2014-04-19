

def write(battlename = None, battlenumber = None):
    if (type(battlename) != "String" ) or (type(battlenumber) != "String"):
        raise Error("bad arguments")
    
    
