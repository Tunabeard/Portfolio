from itertools import permutations

QUEEN_UNIT = "\u2B1C"
SPACE_UNIT = "\u2B1B"

def is_the_board_valid(board):
    queens_indexes = []
    battlefield = []
    while len(battlefield) < 56:
        battlefield.append(0)
    for queen in board:
        battlefield.insert((board.index(queen) * 8 + queen - 1), queen)
        queens_indexes.append(battlefield.index(queen))
    for queen in board:
        space_up = board.index(queen)
        space_down = 7 - board.index(queen)
        space_left = queen - 1
        space_right = 8 - queen
        space_up_left = min(space_up, space_left)
        space_down_left = min(space_down, space_left)
        space_up_right = min(space_up, space_right)
        space_down_right = min(space_down, space_right)
        cells_under_attack = []     # Не абсолютно, а относительно
        a, b, c, d = 1, 1, 1, 1
        while a <= space_up_left:
            cells_under_attack.append(a * -9)
            a += 1
        while b <= space_down_left:
            cells_under_attack.append(b * 7)
            b += 1
        while c <= space_up_right:
            cells_under_attack.append(c * -7)
            c += 1
        while d <= space_down_right:
            cells_under_attack.append(d * 9)
            d += 1
        for operator in cells_under_attack:
            if battlefield.index(queen) + operator in queens_indexes:
                return False
    return True

def numbers_to_graphic(board):
    battlefield = []
    while len(battlefield) < 56:
        battlefield.append(0)
    for item in board:
        battlefield.insert((board.index(item) * 8 + item - 1), item)
    n = 0
    while n < len(battlefield):
        if battlefield[n] == 0:
            battlefield[n] = SPACE_UNIT
        else:
            battlefield[n] = QUEEN_UNIT
        n += 1
    return battlefield

variations = list(permutations([1, 2, 3, 4, 5, 6, 7, 8]))
correct_answers = []

for variation in variations:
    if is_the_board_valid(variation):
        correct_answers.append(variation)

for answer in correct_answers:
    print(str(correct_answers.index(answer) + 1) + ") " + str(answer))

while True:
    request = int(input("Введите номер ответа для просмотра доски: "))
    n = 0
    for cell in numbers_to_graphic(correct_answers[request - 1]):
        print(cell, end="")
        if n in range(7, 64, 8):
            print()
        n += 1