def divisible_by(numbers, divisor):
    arr = []
    for i in range(0, len(numbers)):
        if numbers[i] % divisor == 0:
            arr.append(numbers[i])
    return arr
