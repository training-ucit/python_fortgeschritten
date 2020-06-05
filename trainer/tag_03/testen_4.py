import my_lib

def test_multiply_3_4():
        assert my_lib.multiply(3, 4) == 12

def test_multiply_3_a():
        assert my_lib.multiply(3, "a") == "aaa"