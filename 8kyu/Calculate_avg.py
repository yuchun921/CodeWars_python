def find_average(numbers):
    sum = 0
    if len(numbers) == 0:
        return 0
    else:
        for i in range(len(numbers)):
            sum = sum+numbers[i]
        avg = sum/len(numbers)
        return avg
