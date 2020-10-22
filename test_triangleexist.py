from Triangle import  Triangle

def test_tiangle_exist_positive_points():
    t = Triangle(1, 1, 1, 5, 5, 1)
    result = t.triangleExist()
    assert result == True

def test_tiangle_exist_negative_points():
    t = Triangle(-1, -2, -2, -7, -4, -16)
    result = t.triangleExist()
    assert result == True

def test_tiangle_degenerate():
    t = Triangle(0, 1, 0, 7, 0, 3)
    result = t.triangleExist()
    assert result == True

def test_tiangle_one_point():
    t = Triangle(0, 0, 0, 0, 0, 0)
    result = t.triangleExist()
    assert result == False

def test_tiangle_two_point_one_point():
    t = Triangle(0, 2, 0, 2, 0, 7)
    result = t.triangleExist()
    assert result == False