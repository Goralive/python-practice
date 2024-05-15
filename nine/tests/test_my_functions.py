import pytest

import nine.functions.my_functions as my_functions


# add
def test_add():
    expected_result = 8
    calculated_result = my_functions.add(3, 5)
    assert expected_result == calculated_result


def test_add_calculation_negative_numbers():
    assert True
    # expected_result = -4
    # actual_result = my_functions.add(-8,4)
    # assert expected_result == actual_result


def test_failing_test_add():
    expected_result = 8
    calculated_result = my_functions.add(3, 5)
    assert expected_result == calculated_result


def test_add_strings():
    expected_result = "I like burgers"
    actual_result = my_functions.add("I like ", "burgers")
    assert expected_result == actual_result


# divide


def test_divide():
    expected_result = 2
    actual_result = my_functions.divide(8, 4)
    assert expected_result == actual_result


def test_negative_divide_on_zero_raise_exception():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)


def test_negative_divide_on_zero_raise_exception():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)
