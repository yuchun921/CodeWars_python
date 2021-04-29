def odds(x):
    arr = []
    for i in x:
        if i % 2 != 0:
            arr.append(i)
    return arr
