from hello import main


def test_main(capsys, monkeypatch, tmp_path):
    # Мокаем input
    monkeypatch.setattr("builtins.input", lambda _: "Иван")

    # Вызываем тестируемую функцию
    main()

    # Проверяем вывод в stdout
    captured = capsys.readouterr()
    assert "Привет, Иван!" in captured.out

    # Проверяем содержимое файла
    with open("hello.txt", encoding="utf-8") as f:
        assert "Привет, Иван!" in f.read()
