from roman_to_arabic import transform


def test_transform_simple():
    pairs = [
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("V", 5),
        ("VI", 6),
        ("X", 10),
        ("XXI", 21),
        ("XIX", 19),
        ("L", 50),
        ("C", 100),
        ("D", 500),
        ("M", 1000)
    ]

    for roman_number, arab_number in pairs:
        assert transform(roman_number) == arab_number


def test_four_works():
    assert transform("IV") == 4


def test_nine_works():
    assert transform("IX") == 9


def test_forty_works():
    assert transform("XL") == 40


def test_ninety_works():
    assert transform("XC") == 90


def test_four_hundred_works():
    assert transform("CD") == 400


def test_nine_hundred_works():
    assert transform("CM") == 900


def test_homework():
    for roman, arab in [
        ("MCMLXXXIX", 1989),
        ("MCMLVII", 1957),
        ("MCM", 1900),
        ("MDCCCLVII", 1857),
        ("MCMXCIX", 1999),
        ("CCCLXXXVIII", 388),
        ("CDXLIX", 449)
    ]:
        assert transform(roman) == arab
