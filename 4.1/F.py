summ = 0
def move(player, number):
    global summ
    if player == "Петя":
        summ += number
    else:
        summ -= number
def game_over():
    if summ < 0:
        print("Ваня")
    elif summ > 0:
        print("Петя")
    else:
        print("Ничья")

move('Петя', 3)
move('Ваня', 4)
move('Петя', 4)
move('Ваня', 3)
game_over()