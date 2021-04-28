def stringy(size):
    result = ''
    for i in range(size):
        if i % 2 == 0:
            result = result+'1'
        else:
            result = result+'0'
    return result
