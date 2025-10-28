from nameExcept import ZeroNameLengthError,SpaceError,InvalidNameError
def validatename(name):
    if(len(name)==0):
        raise ZeroNameLengthError
    elif(name.isspace()):
        raise SpaceError
    else:
        res = True
        words = name.split()
        for word in words:
            if(not word.isalpha()):
                res = False
                break
            if(res):
                return name
            else:
                raise InvalidNameError