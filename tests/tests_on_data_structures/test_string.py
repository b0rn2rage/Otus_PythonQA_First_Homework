import pytest


class TestStr:
    @staticmethod
    def check_isalpha(input_str: str):
        assert input_str.isdigit()

    @staticmethod
    def check_strip(input_str: str, result: str):
        assert input_str.strip() == result, f"Строка {input_str.strip()} != {result}"

    @staticmethod
    def check_count(input_str: str, symbol: str):
        result = input_str.count(symbol)
        print(result)
        assert result == input_str.count(symbol), \
            f"В строке {input_str} количество повторений символа = {symbol} != {result}"

    @staticmethod
    def check_join(input_list: list, separator: str):
        result = separator.join(input_list)
        print(result)
        assert result == separator.join(input_list)

    @staticmethod
    def check_len(input_str: str, expected_len: int):
        result = len(input_str)
        print("Длина строки =", result)
        assert result == expected_len, f"Длина строки {input_str} не соответствует ожидаемой длине {expected_len}"


def test_isdigit_method():
    TestStr.check_isalpha("123123")


def test_check_strip_method():
    TestStr.check_strip("   qweqwe   ", "qweqwe")


@pytest.mark.parametrize('symbol', ("a", "b", "c", "d", " "))
def test_check_count_method(symbol):
    TestStr.check_count("abcda", symbol)


def test_check_join_method():
    TestStr.check_join(["За", "окном", "идёт", "снег"], "***")


def test_check_len_method():
    TestStr.check_len("Три", 3)
