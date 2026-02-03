# Python Max Course

Курс по Python с акцентом на практические задания и тестирование.

## 🚀 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/python-max-course.git
   cd python-max-course
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Запуск тестов

```bash
pytest
```

## 📚 Содержимое проекта

### Функции в [src/utils.py](cci:7://file:///c:/Users/lebed/Desktop/Learn/python-max-course/src/utils.py:0:0-0:0):

- [unique_sorted(nums)](cci:1://file:///c:/Users/lebed/Desktop/Learn/python-max-course/src/utils.py:4:0-14:28) - возвращает отсортированный список уникальных чисел
- [char_counter(text)](cci:1://file:///c:/Users/lebed/Desktop/Learn/python-max-course/src/utils.py:21:0-37:34) - подсчитывает количество вхождений каждого символа в тексте
- [square_even(nums)](cci:1://file:///c:/Users/lebed/Desktop/Learn/python-max-course/src/utils.py:14:0-18:46) - возвращает список квадратов четных чисел
- [top_n_common(chars, n=5)](cci:1://file:///c:/Users/lebed/Desktop/Learn/python-max-course/src/utils.py:36:0-38:76) - находит N самых частых символов
- [calc_avg(numbers, ignore_zero=False)](cci:1://file:///c:/Users/lebed/Desktop/Learn/python-max-course/src/utils.py:47:0-79:40) - вычисляет среднее арифметическое

### Тесты

- `tests/test_avg.py` - тесты для функции [calc_avg](cci:1://file:///c:/Users/lebed/Desktop/Learn/python-max-course/src/utils.py:47:0-79:40)
- [tests/test_comprehensions.py](cci:7://file:///c:/Users/lebed/Desktop/Learn/python-max-course/tests/test_comprehensions.py:0:0-0:0) - тесты для функций работы с коллекциями

## 🤝 Вклад в проект

1. Создайте ветку для новой фичи: `git checkout -b feature/feature-name`
2. Сделайте коммиты: `git commit -m "feat: add new feature"`
3. Отправьте изменения: `git push -u origin feature/feature-name`
4. Создайте Pull Request

## 📝 Лицензия

MIT