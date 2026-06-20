in_stock = {"coffee": 1, "milk": 2, "cream": 3}
recipe = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1}
}


def order(*args):
    global in_stock

    for drink in args:
        can_make = True

        for ingredient, amount in recipe[drink].items():
            if in_stock.get(ingredient, 0) < amount:
                can_make = False
                break

        if can_make:
            for ingredient, amount in recipe[drink].items():
                in_stock[ingredient] -= amount

            return drink

    return "К сожалению, не можем предложить Вам напиток"

print(order("Капучино"))