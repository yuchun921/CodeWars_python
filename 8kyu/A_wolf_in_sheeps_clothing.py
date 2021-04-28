def warn_the_sheep(queue):
    count = len(queue)
    if queue[len(queue)-1] == 'wolf':
        return "Pls go away and stop eating my sheep"

    for i in range(len(queue)):
        count = count-1
        if queue[i] == 'wolf':
            return f'Oi! Sheep number {count}! You are about to be eaten by a wolf!'
