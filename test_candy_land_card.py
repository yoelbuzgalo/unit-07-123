import candy_land_card
import random

def test_make_deck_len():
    # Setup
    expected = 67

    # Invoke
    result = len(candy_land_card.make_deck())

    # Analysis
    assert result == expected

def test_single_cards_R():
    # Setup
    expected = (1, 'R', 'SR')

    # Invoke
    result = candy_land_card.make_deck()

    # Analysis
    assert result[0] == expected

def test_single_cards_P():
    # Setup
    expected = (1, 'P', 'SP')

    # Invoke
    result = candy_land_card.make_deck()

    # Analysis
    assert result[1] == expected

def test_single_cards_Y():
    # Setup
    expected = (1, 'Y', 'SY')

    # Invoke
    result = candy_land_card.make_deck()

    # Analysis
    assert result[2] == expected


def test_double_cards_B():
    # Setup
    expected = (2, 'B', 'DB')

    # Invoke
    result = candy_land_card.make_deck()

    # Analysis
    assert result[39] == expected

def test_double_cards_O():
    # Setup
    expected = (2, 'O', 'DO')

    # Invoke
    result = candy_land_card.make_deck()

    # Analysis
    assert result[40] == expected

def test_special_cards():
    # Setup
    expected = (117, 'X', "BB")

    # Invoke
    result = candy_land_card.make_deck()

    # Analysis
    assert result[-1] == expected

def test_shuffle_cards_17():
    # Setup
    random.seed(1)
    deck = candy_land_card.make_deck()
    expected = deck[17]

    # Invoke
    result = candy_land_card.shuffle(candy_land_card.make_deck())

    # Analysis
    assert result[0] == expected

# def test_shuffle_cards_8():
#     # Setup
#     random.seed(1)
#     deck = candy_land_card.make_deck()
#     expected = (1, 'Y', 'SY')

#     # Invoke
#     result = candy_land_card.shuffle(deck)

#     # Analysis
#     assert result[8] == expected

# def test_shuffle_cards_32():
#     # Setup
#     random.seed(1)
#     deck = candy_land_card.make_deck()
#     expected = (1, 'Y', 'SY')

#     # Invoke
#     result = candy_land_card.shuffle(deck)

#     # Analysis
#     assert result[32] == expected
    