def sum_numbers(num1, num2):
    return num1 + num2


def test_sum():
    num1 = 5
    num2 = 7
    expected_result = 12

    result = sum_numbers(num1, num2)

    assert (
        result == expected_result
    ), f"Sum of {num1} and {num2} should be {expected_result}"
