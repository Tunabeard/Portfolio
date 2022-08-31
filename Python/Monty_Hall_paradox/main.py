import random

ITERATIONS = 1000000

def monty_hall_paradox(iterations):
    change_wins, change_loses, keep_wins, keep_loses = 0, 0, 0, 0
    n = 0
    while n < iterations:
        correct_door = random.randint(1, 3)
        first_choice = random.randint(1, 3)
        if first_choice != correct_door:
            change_wins += 1
        else:
            change_loses += 1
        n += 1
    n = 0
    while n < iterations:
        correct_door = random.randint(1, 3)
        first_choice = random.randint(1, 3)
        if first_choice == correct_door:
            keep_wins += 1
        else:
            keep_loses += 1
        n += 1
    return [change_wins, change_loses, keep_wins, keep_loses]

print("Подождите...")
answers = monty_hall_paradox(ITERATIONS)

print("\nЕсли менять выбор:\nИз " + str(ITERATIONS) + " итераций " + str(answers[0]) + " оказались выигрышными и " + str(answers[1]) + " оказались проигрышными.")
print("\nЕсли НЕ менять выбор:\nИз " + str(ITERATIONS) + " итераций " + str(answers[2]) + " оказались выигрышными и " + str(answers[3]) + " оказались проигрышными.")