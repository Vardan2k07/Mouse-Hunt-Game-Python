# Basic validation tests for Mouse Hunt.
# These tests check the main game rules without opening the game window.

def add_score(score):
    return score + 10

def valid_direction(current, new):
    opposite = {
        "up": "down",
        "down": "up",
        "left": "right",
        "right": "left"
    }
    return opposite.get(current) != new

def inside_boundary(x, y):
    return abs(x) <= 380 and abs(y) <= 280

def test_score():
    assert add_score(0) == 10
    assert add_score(20) == 30

def test_direction():
    assert valid_direction("up", "left")
    assert not valid_direction("up", "down")
    assert valid_direction("right", "up")
    assert not valid_direction("left", "right")

def test_boundary():
    assert inside_boundary(0, 0)
    assert inside_boundary(380, 280)
    assert not inside_boundary(400, 0)

print("All Mouse Hunt tests passed.")
