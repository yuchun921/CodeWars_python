def rental_car_cost(d):
    price = 0
    if d >= 7:
        price = 40*d-50
    elif d >= 3:
        price = 40*d-20
    else:
        price = 40*d
    return price
