def no_space(x):
    char = ''
    for i in range(len(x)):
        if x[i] == ' ':
            continue
        else:
            char = char + x[i]
    return char
