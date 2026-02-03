from typing import List, Dict, Tuple, Iterable


def unique_sorted(nums: List[int]) -> List[int]:
    """
    Возвращает отсортированный список без дублирования.
    """
    # Параллельно демонстрируем альтернативный синтаксис { *nums }
    return sorted({*nums})


def square_even(nums: List[int]) -> List[int]:
    """
    Возвращает список квадратов чётных чисел.
    """
    return [x * x for x in nums if x % 2 == 0]


def char_counter(text: str, ignore_case: bool = True) -> Dict[str, int]:
    """
    Подсчитывает количество символов в строке (без пробелов и пунктуации).

    Parameters
    ----------
    text : str
        Исходный текст.
    ignore_case : bool, optional
        Игнорировать регистр, по умолчанию True.
    """
    # Приводим к нижнему регистру, если требуется
    work = text.lower() if ignore_case else text

    # отбрасываем пробелы и знаки пунктуации
    filtered = (c for c in work if c.isalpha())
    return dict(Counter(filtered))


def top_n_common(chars: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    """
    Возвращает n самых часто встречающихся символов.
    """
    return sorted(chars.items(), key=lambda item: item[1], reverse=True)[:n]


def calc_avg(numbers: Iterable[int | float], ignore_zero: bool = False) -> float:
    """
    Среднее арифметическое последовательности.

    Parameters
    ----------
    numbers : iterable of int/float
        Исходные значения.
    ignore_zero : bool, optional
        Не учитывать нули (по умолчанию False).

    Returns
    -------
    float
        Среднее значение.

    Raises
    ------
    ZeroDivisionError
        Если после фильтрации набор пустой.
    """
    # 1️⃣ Фильтрация нулей, если требуется
    if ignore_zero:
        filtered = [x for x in numbers if x != 0]
    else:
        filtered = list(numbers)

    # 2️⃣ Проверка на пустой набор
    if not filtered:
        raise ZeroDivisionError("empty sequence after filtering")

    # 3️⃣ Вычисление среднего
    return sum(filtered) / len(filtered)
