import pytest
from string_utils import StringUtils


string_utils = StringUtils()


'''
Принимает на вход текст, делает первую букву заглавной
и возвращает этот же текст
'''


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ('skypro', 'Skypro'),  # одно слово
    ('hello world', 'Hello world'),  # пробел в середине
    ('a', 'A'),  # одна буква
    ('STUDENT', 'Student'),  # все заглавные буквы
    ('quAlITy AsSuRanCe', 'Quality assurance'),  # разный регистр
    ('list of products: bread, milk.', 'List of products: bread, milk.'),
    # предложение с символами, пробелами
    ('Engineer', 'Engineer'),  # первая буква заглавная изначально
    ('mom ', 'Mom '),  # пробел в конце
    ('май 2025 года', 'Май 2025 года')  # строка с пробелами и цифрами
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ('1abc', '1abc'),  # первый символ цифра
    ('89829061475', '89829061475'),  # только цифры
    ('', ''),  # пустая строка
    ('   ', '   '),  # только пробелы
    ('!hello', '!hello'),  # первый спецсимвол
    (' positive', ' positive'),  # первый пробел

])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


'''
Принимает на вход текст и удаляет пробелы в начале, если они есть.
'''


@pytest.mark.positive
@pytest.mark.parametrize('input_str, expected', [
    (' skypro', 'skypro'),  # удаление пробела в начале строки
    ('  hello', 'hello'),  # несколько пробелов в начале строки
    (' I Love You ', 'I Love You '),
    # строка с пробелами в начале, в середине и в конце строки
    ('dad', 'dad')  # отсутствие пробела в начале строки
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, expected', [
    ('   ', ''),  # строка состоит только из пробелов
    ('', '')  # пустая строка
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


'''
Возвращает `True`, если строка содержит искомый символ
и `False` - если нет
Параметры:
`string` - строка для обработки
`symbol` - искомый символ
'''


@pytest.mark.positive
@pytest.mark.parametrize('input_str, input_symbol, expected', [
    ('hello world', 'h', True),  # найден символ в начале строки
    ('python', 'th', True),  # найден символ в середине строки
    ('skyeng', 'g', True),  # найден символ в конце строки
    ('makaka', 'a', True),  # найдено несколько символов в строке
    ('Adversary', 'A', True),  # найден символ другого регистра
    ('89829061548', '1548', True),  # нахождение цифры в строке
    ('quality control', ' ', True),  # нахождение пробела
    ('%&^#@:]', '#', True),  # нахождение специального символа
    ('q', 'q', True),  # строка из одного символа
    ('xxxxx', 'x', True),  # строка состоит из повторяющегося символа
    ('', '', True)  # пустая строка, отсутствие символа
])
def test_contains_positive(input_str: str, input_symbol: str, expected: bool):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, input_symbol, expected', [
    ('hello world', 'a', False),  # отсутствующий символ в строке
    ('Hello', 'h', False),  # нахождение символа другого регистра
    ('15.09.1988', 'u', False),  # поиск буквы в строке с цифрами
    ('Engineer', ' ', False),  # поиск пробела как символа
    ('p', 'k', False)  # строка из одного символа
])
def test_contains_negative(input_str: str, input_symbol: str, expected: bool):
    assert string_utils.contains(input_str, input_symbol) == expected


'''
Удаляет все подстроки из переданной строки
Параметры:
`string` - строка для обработки
`symbol` - искомый символ для удаления
'''


@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol_to_delete, expected', [
    ('student', 'u', 'stdent'),  # символ, который присутствует в строке
    ('happiness', 'h', 'appiness'),  # удаление в начале строки
    ('love', 'e', 'lov'),  # удаление в конце строки
    ('engineer', 'gine', 'ener'),  # удаление в середине строки
    ('amamama', 'ama', 'm'),  # удаление всех вхождений подстроки
    ('python', 'python', ''),  # подстрока совпадает со строкой
    ('ssssss', 's', '')  # повторяющаяся подстрока
])
def test_delete_symbol_positive(input_str, symbol_to_delete, expected):
    assert string_utils.delete_symbol(input_str, symbol_to_delete) == expected


@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol_to_delete, expected', [
    ('study', 'abc', 'study'),  # подстрока отсутствует в строке
    ('', 'son', ''),  # пустая строка
    ('Moscow', '', 'Moscow'),  # пустая подстрока
    ('', '', ''),  # пуста строка и пустая подстрока
    ('SKYPRO', 'sky', 'SKYPRO'),  # различные регистры
    ('interview', 'TER', 'interview')  # различные регистры
])
def test_delete_symbol_negative(input_str, symbol_to_delete, expected):
    assert string_utils.delete_symbol(input_str, symbol_to_delete) == expected
