def abbrev_name(name):
    s = name[0:1].upper()
    for i in range(len(name)):
        if name[i] == ' ':
            n = name[i+1].upper()
    chr = s+'.'+n
    return chr
