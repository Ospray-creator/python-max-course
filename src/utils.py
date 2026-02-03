import string
from typing import List, Dict, Tuple


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
    return {
        char: text.count(char)
        for char in text
        if char not in string.punctuation and char != " "
    }


def top_n_common(chars: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    """Возвращает n самых частых символов"""
    return sorted(chars.items(), key=lambda item: item[1], reverse=True)[:n]
