def numbers_to_graphic(time, are_delimeters_active_now, colored_cell, uncolored_cell):

    digits_graphic_view = {
        "0": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
        "1": ["00100", "01100", "00100", "00100", "00100", "00100", "00100"],
        "2": ["01110", "10001", "00001", "00010", "01100", "10000", "11111"],
        "3": ["01110", "10001", "00001", "01110", "00001", "10001", "01110"],
        "4": ["00010", "00110", "01010", "10010", "11111", "00010", "00010"],
        "5": ["11111", "10000", "11110", "00001", "00001", "10001", "01110"],
        "6": ["01110", "10000", "10000", "01110", "10001", "10001", "01110"],
        "7": ["11111", "00001", "00010", "00100", "01000", "01000", "01000"],
        "8": ["01110", "10001", "10001", "01110", "10001", "10001", "01110"],
        "9": ["01110", "10001", "10001", "01111", "00001", "00001", "01110"]
    }

    clock_raw = ["", "", "", "", "", "", ""]
    digit_index = 0
    for digit in time:
        n = 0
        for item in digits_graphic_view[digit]:
            clock_raw[n] += item
            n += 1
        m = 0
        for line in clock_raw:
            if digit_index in [1, 3]:
                clock_raw[m] += "000"
            elif digit_index in [0, 2, 4]:
                clock_raw[m] += "0"
            m += 1
        digit_index += 1

    if are_delimeters_active_now:
        clock_raw[1] = clock_raw[1][:12] + "1" + clock_raw[1][13:26] + "1" + clock_raw[1][27:]
        clock_raw[5] = clock_raw[5][:12] + "1" + clock_raw[5][13:26] + "1" + clock_raw[5][27:]
    
    clock_ready = []
    for line in clock_raw:
        clock_ready.append(line.replace("1", colored_cell).replace("0", uncolored_cell))

    return clock_ready