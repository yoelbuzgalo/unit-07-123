import candy_land

def test_create_board_len():
    # Setup
    expected = 134

    # Invoke
    result = len(candy_land.create_board())

    # Analysis
    assert result == expected

def test_create_board_first():
    # Setup
    expected = 'R'

    # Invoke
    result = candy_land.create_board()

    # Analysis
    assert result[0] == expected

def test_create_board_special_char():
    # Setup
    expected = 'CC'

    # Invoke
    result = candy_land.create_board()

    # Analysis
    assert result[9] == expected

def test_create_board_normal():
    # Setup
    expected = 'O'

    # Ivoke
    result = candy_land.create_board()

    # Analysis
    assert result[10] == expected

def test_create_board_end():
    # Setup
    expected = 'MC'

    # Invoke
    result = candy_land.create_board()

    #Analysis
    assert result[133] == expected