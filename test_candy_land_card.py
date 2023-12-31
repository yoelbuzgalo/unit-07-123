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
    result = candy_land_card.shuffle(deck)

    # Analysis
    assert result[0] == expected

def test_shuffle_cards_8():
    # Setup
    random.seed(1)
    deck = candy_land_card.make_deck()
    expected = deck[8]

    # Invoke
    result = candy_land_card.shuffle(deck)

    # Analysis
    assert result[1] == expected

def test_shuffle_cards_32():
    # Setup
    random.seed(1)
    deck = candy_land_card.make_deck()
    expected = deck[32]

    # Invoke
    result = candy_land_card.shuffle(deck)

    # Analysis
    assert result[2] == expected

def test_draw_card_empty():
    # Setup
    deck = []
    expected = None

    # Invoke
    result = candy_land_card.draw(deck) 

    # Analysis
    assert result == expected

def test_draw_card_regular_deck():
    # Setup
    deck = candy_land_card.make_deck()
    expected = deck[-1]

    # Invoke
    result = candy_land_card.draw(deck)

    assert result == expected

def test_draw_card_shuffled_deck():
    # Setup
    deck = candy_land_card.make_deck()
    shuffled_deck = candy_land_card.shuffle(deck)
    expected = shuffled_deck[-1]

    # Invoke
    result = candy_land_card.draw(shuffled_deck)

    assert result == expected

def test_draw_card_shuffled_deck_second():
    # Setup
    deck = candy_land_card.make_deck()
    shuffled_deck = candy_land_card.shuffle(deck)
    expected = shuffled_deck[-2]

    # Invoke
    candy_land_card.draw(shuffled_deck) # Invoke first draw
    result = candy_land_card.draw(shuffled_deck) # Invoke second draw

    assert result == expected