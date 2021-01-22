import pytest


class TestSet:
    @staticmethod
    def check_isdisjoint(input_set: set, other: set):
        result = input_set.isdisjoint(other)
        print(input_set, other)
        assert result is True, f"В множествах {input_set} и {other} есть одинаковые элементы"

    @staticmethod
    def check_issubset(input_set: set, other: set):
        result = input_set.issubset(other)
        print(input_set, other)
        assert result is True, f"Элементы {input_set} не принадлежат множеству {other}"

    @staticmethod
    def check_issuperset(input_set: set, other: set):
        result = input_set.issuperset(other)
        print(input_set, other)
        assert result is True, f"Элементы {other} не принадлежат множеству {input_set}"

    @staticmethod
    def check_union(first_set: set, second_set: set, third_set: set):
        result = first_set.union(second_set, third_set)
        print(result)
        assert first_set.issubset(result) and second_set.issubset(result) and third_set.issubset(
            result), f"В множество {first_set} не были добавлены другие множества"

    @staticmethod
    def check_pop(input_set: set):
        start_len = len(input_set)
        print("До удаления элемента:", input_set)
        input_set.pop()
        print("После удаления первого элемента:", input_set)
        finish_len = len(input_set)
        assert finish_len == start_len - 1, f"Длина множества до и после удаления первого элемента должна различаться"


@pytest.mark.parametrize('other', [{4}, {5}, {6}, {7}, {8}])
def test_isdisjoint_method(other):
    TestSet.check_isdisjoint({1, 2, 3}, other)


def test_issubset_method():
    TestSet.check_issubset({1, 2, 3}, {1, 2, 3, 4})


def test_issuperset_method():
    TestSet.check_issuperset({1, 2, 3, 4}, {1, 2, 3})


def test_union_method():
    TestSet.check_union({1}, {1, 2}, {3, 3, 4})


def test_pop_method():
    TestSet.check_pop({1, 2, 3, 4, 5})