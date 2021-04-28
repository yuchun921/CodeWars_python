def solution(string):
    arr = []
    for i in range(len(string)):
        arr.append(string[i])

    return ''.join(reversed(arr))
