def transform(roman_numeral: str) -> int:
    arab_number = 0
    for i in range(0, len(roman_numeral)):
        roman_digit = roman_numeral[i]
        future_roman_digit = None
        try:
            future_roman_digit = roman_numeral[i+1]
        except IndexError:
            pass

        if roman_digit == "I":
            if future_roman_digit == "V" or future_roman_digit == "X":
                arab_number -= 1
            else:
                arab_number += 1
        if roman_digit == "V":
            arab_number += 5
        if roman_digit == "X":
            if future_roman_digit == "L" or future_roman_digit == "C":
                arab_number -= 10
            else:
                arab_number += 10
        if roman_digit == "L":
            arab_number += 50
        if roman_digit == "C":
            if future_roman_digit == "D" or future_roman_digit == "M":
                arab_number -= 100
            else:
                arab_number += 100
        if roman_digit == "D":
            arab_number += 500
        if roman_digit == "M":
            arab_number += 1000

    return arab_number
