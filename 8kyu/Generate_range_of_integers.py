def generate_range(min, max, step):
    result = []
    for i in range(min, max + 1, step):
        result.append(i)
    return result
