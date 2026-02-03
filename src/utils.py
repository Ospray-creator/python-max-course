from typing import List, Dict, Tuple, Iterable


def unique_sorted(nums: List[int]) -> List[int] | None:
    """Возвращает отсортированный список уникальных чисел.

    Пример
    ------
    >>> unique_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    if not nums:
        return None
    return sorted(set(nums))


def char_counter(text: str) -> Dict[str, int]:
    """Возвращает словарь с количеством вхождений каждого символа в тексте.

    Пример
    ------
    >>> char_counter("Hello, World!")
    {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

    Использует dict comprehension.

    Игнорируй пробелы и знаки пунктуации (string.punctuation).
    """
    text_lower = text.lower()
    return {
        char: text_lower.count(char)
        for char in text_lower
        if char not in string.punctuation and char != " "
    }


def top_n_common(chars: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    """Возвращает n самых частых символов"""
    return sorted(chars.items(), key=lambda item: item[1], reverse=True)[:n]


def calc_avg(numbers: Iterable[int | float], ignore_zero: bool = False) -> float:
    """
    Возвращает среднее арифметическое значений в ``numbers``.
    Если ``ignore_zero`` == True – нули в набор не учитываются.

    Использует list comprehension.
    """
    if ignore_zero:
        numbers = [num for num in numbers if num != 0]
    if not numbers:
        raise ZeroDivisionError("Нельзя подсчитать среднее пустого набора")
    return sum(numbers) / len(numbers)
