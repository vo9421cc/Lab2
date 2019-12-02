def createMenu(optionlist):
    tmp = ''; ct = 0
    for opt in optionlist:
        tmp += str(ct) +'.' + opt + '\n'
        ct += 1
    return tmp
