def merge_arrays(arr1, arr2):
    result = []
    for i in arr1:
        if i not in result:
            result.append(i)
    for i in arr2:
        if i not in result:
            result.append(i)
    result.sort()
    return result
