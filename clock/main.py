from functions_file import numbers_to_graphic
import os
import time
import datetime
clear = lambda: os.system("cls")

CONSTRUCTION_UNIT = "\u2B1C"
SPACE_UNIT = "\u2B1B"
are_delimeters_active_now = False

while True:
    clear()
    current_time = datetime.datetime.now().strftime("%H%M%S")
    clock = numbers_to_graphic(current_time, are_delimeters_active_now, CONSTRUCTION_UNIT, SPACE_UNIT)

    for line in clock:
        print(line)

    are_delimeters_active_now = not are_delimeters_active_now
    time.sleep(1)