def is_vow(inp):
    l = []
    for each in inp:
        if each == 97:
            l.append('a')
        elif each == 101:
            l.append('e')
        elif each == 105:
            l.append('i')
        elif each == 111:
            l.append('o')
        elif each == 117:
            l.append('u')
        else:
            l.append(each)
    return l
