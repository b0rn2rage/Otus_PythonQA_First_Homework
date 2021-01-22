import pytest


class TestList:
    @staticmethod
    def check_append(input_list: list, item_to_be_added):
        """Тест для проверки метода append.

        :param input_list: Входной список
        :param item_to_be_added: Добавляемый элемент
        """
        input_list.append(item_to_be_added)
        print(input_list)
        assert input_list[-1] == item_to_be_added, \
            f"Последний элемент списка = {input_list[-1]} и он != элементу добавленному с помощью append"

    @staticmethod
    def check_extend(input_list: list, list_to_add: list):
        """Тест для проверки метода extend.

        :param input_list: Входной список
        :param list_to_add: Добавляемый список
        """
        input_list.extend(list_to_add)
        print(input_list)
        assert input_list[-(len(list_to_add)):] == list_to_add, \
            f"Список {input_list} не расширен элементами {list_to_add}"

    @staticmethod
    def check_insert(input_list: list, index: int, insert_the_element):
        """Тест для проверки метода insert.

        :param input_list: Входной список
        :param index: Индекс перед которым нужно вставить элемент
        :param insert_the_element: Вставляемый элемент
        """
        input_list.insert(index, insert_the_element)
        print(input_list)
        assert input_list[index] == insert_the_element, \
            f"Элемент {insert_the_element} не находится на позиции {input_list[index]}"

    @staticmethod
    def check_clear(input_list: list):
        """Тест для проверки метода clear.

        :param input_list: Входной список
        """
        input_list.clear()
        print('input_list =', input_list)
        assert input_list == [], f"Список {input_list} не пустой"

    @staticmethod
    def check_sort(input_list: list):
        """Тест для проверки метода sort (сортировка по возрастанию).

        :param input_list: Входной список
        """
        input_list.sort()
        print(input_list)
        assert min(input_list) == input_list[
            0], f'Первый элемент списка {input_list} не является минимальным элеметом списка'


@pytest.mark.parametrize('item', ('q', 'WE', '-1', '0', 'TEST'))
def test_append_method(item):
    TestList.check_append([1, 2, 3, 4, 5], item)


def test_extend_method():
    TestList.check_extend([1, 2, 3, 4, 5], ['q', 'w', 'e', 'r', 't', 'y'])


def test_insert_method():
    TestList.check_insert([1, 2, 4, 5], 2, 3)


def test_clear_method():
    TestList.check_clear([1, 2, 3, 4, 5])


def test_sort_method():
    TestList.check_sort(['c', 'a', 'bwe'])
