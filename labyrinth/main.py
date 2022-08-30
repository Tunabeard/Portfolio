import random
import os
clear = lambda: os.system("cls")

STARTFINISH_UNIT = "\u2B50"
ROAD_UNIT = "\u2B1B"
WALL_UNIT = "\u2B1C"

def create_labyrinth(size):

    def generate_new_way(cell, are_crossroads_allowed):
        expand_indexes = {
            "u": [cell - labyrinth_border_size, cell - labyrinth_border_size * 2],
            "d": [cell + labyrinth_border_size, cell + labyrinth_border_size * 2],
            "l": [cell - 1, cell - 2],
            "r": [cell + 1, cell + 2]
        }
        available_expand_directions = []
        if cell - size * 2 > 0 and labyrinth[cell - size * 2] not in [1, 2]:
            available_expand_directions.append("u")
        if cell + size * 2 < len(labyrinth) and labyrinth[cell + size * 2] not in [1, 2]:
            available_expand_directions.append("d")
        if cell % size != 1 and labyrinth[cell - 2] not in [1, 2]:
            available_expand_directions.append("l")
        if cell % size != size - 2 and labyrinth[cell + 2] not in [1, 2]:
            available_expand_directions.append("r")
        
        if len(available_expand_directions) == 0:
            cells_to_expand.remove(cell)
            return

        if are_crossroads_allowed:
            if len(available_expand_directions) >= 2:
                available_expand_directions.append(available_expand_directions[0] + available_expand_directions[1])
            if len(available_expand_directions) == 3:
                available_expand_directions.append(available_expand_directions[0] + available_expand_directions[2])
                available_expand_directions.append(available_expand_directions[1] + available_expand_directions[2])
                available_expand_directions.append(available_expand_directions[0] + available_expand_directions[1] + available_expand_directions[2])

        new_direction = random.choice(available_expand_directions)
        for direction_unit in new_direction:
            for new_road_cell in expand_indexes[direction_unit]:
                labyrinth[new_road_cell] = 1
                correct_way.append(new_road_cell)
                cells_to_expand.append(expand_indexes[direction_unit][1])

    labyrinth = []
    correct_way = [labyrinth_border_size + 1]
    while len(labyrinth) < labyrinth_border_size**2:
        labyrinth.append(0)
    labyrinth[labyrinth_border_size] = 3                                    # Создание "входа" в лабиринт
    labyrinth[len(labyrinth) - labyrinth_border_size - 1] = 3               # Создание "выхода" из лабиринта
    labyrinth[labyrinth_border_size + 1] = 1                                # Создание ближайшей ко "входу" клетки с дорожкой
    cells_to_expand = [labyrinth_border_size + 1]                           # Массив будет хранить все клетки с дорожкой, от которых дорожку можно расширять. По умолчанию хранит ту единственную, что описана выше

    while labyrinth[len(labyrinth) - labyrinth_border_size - 2] != 1:       # Цикл работает до тех пор, пока рядом с "выходом" не появится дорожка — это будет означать, что маршрут построен
        correct_way_fixed = []
        for item in correct_way:
            if correct_way.index(item) <= correct_way.index(cells_to_expand[-1]):
                correct_way_fixed.append(item)
        correct_way = correct_way_fixed
        generate_new_way(cells_to_expand[-1], False)                        # Создание единственного правильного маршрута от "входа" к "выходу"; перекрёстки на этом этапе не создаются

    for correct_road_cell in correct_way:
        labyrinth[correct_road_cell] = 2                                    # Все единицы в лабиринте заменяются на двойки — так программа запомнит правильный маршрут

    while len(cells_to_expand) > 0:
        generate_new_way(random.choice(cells_to_expand), True)

    return labyrinth

def print_puzzle(puzzle, user_asked_for_answer):
    clear()
    n = 0
    for cell in puzzle:
        if cell == 0:
            print(WALL_UNIT, end="")
        elif cell == 3:
            print(STARTFINISH_UNIT, end="")
        else:
            if user_asked_for_answer and cell == 2:
                print(STARTFINISH_UNIT, end="")
            else:
                print(ROAD_UNIT, end="")
        if n in range(labyrinth_border_size-1, len(puzzle), labyrinth_border_size):
            print()
        n += 1

clear()
while True:
    try:
        labyrinth_border_size = int(input("Введите размер лабиринта (подойдут только натуральные нечётные числа от 3 до 49): "))
        if labyrinth_border_size not in range(3, 50, 2):
            print("Ваше число не подходит.")
            continue
        break
    except:
        print("Вы должны ввести число. Это не число.")

print("\nПожалуйста, подождите, лабиринт создаётся. Это может занять некоторое время...")
labyrinth = create_labyrinth(labyrinth_border_size)
print_puzzle(labyrinth, False)

request = input("Нажмите Enter, чтобы увидеть путь.")
if len(request) >= 0:
    print_puzzle(labyrinth, True)