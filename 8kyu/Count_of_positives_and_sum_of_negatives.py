def count_positives_sum_negatives(arr):
    p = 0
    n = 0
    ar = []
    if len(arr) == 0:
        return ar
    for i in range(0, len(arr)):
        if arr[i] > 0:
            p = p+1
        elif arr[i] < 0:
            n = n+arr[i]
    ar.append(p)
    ar.append(n)

    return ar