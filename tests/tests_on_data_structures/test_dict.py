import pytest


class TestDict:
    @staticmethod
    def check_get(input_dict: dict, key: str):
        result = input_dict.get(key)
        print(result)
        assert result == input_dict[key], f"Значение ключа {key} != {result}"

    @staticmethod
    def check_pop(input_dict: dict, key: str):
        result = input_dict.pop(key)
        print(result)
        assert result not in input_dict.values(), f"Значение {result} присутствует в {input_dict.values()}"

    @staticmethod
    def check_clear(input_dict: dict):
        input_dict.clear()
        print('input_dict =', input_dict)
        assert input_dict == {}, f"Словарь {input_dict} не пустой"

    @staticmethod
    def check_copy(input_dict: dict):
        copy_dict = input_dict.copy()
        assert input_dict == copy_dict, f"Словарь {input_dict} != {copy_dict}"

    @staticmethod
    def check_popitem(input_dict: dict):
        start_len = len(input_dict)
        print('Начальная длина словаря:', start_len)
        input_dict.popitem()
        finish_len = len(input_dict)
        print('Длина словаря после удаления одной пары значений:', finish_len)
        assert finish_len == start_len - 1, f'Длина словаря не уменьшилась на единицу'


@pytest.mark.parametrize("key", ("a", "b", "c", "d", "e"))
def test_get_method(key):
    TestDict.check_get({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}, key)


def test_pop_method():
    TestDict.check_pop({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}, "b")


def test_clear_method():
    TestDict.check_clear({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})


def test_copy_method():
    TestDict.check_copy({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})


def test_popitem_method():
    TestDict.check_popitem({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
