def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"];

    if n <= 10:
        s=dogs[0]
    elif n <= 50:
        s=dogs[1]
    elif n == 101:
        s=dogs[3]
    else:
        s=dogs[2]

    return s