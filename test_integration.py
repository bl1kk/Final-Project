import pytest
from mass_converter import main

def test_integration_main(monkeypatch, capsys):
    # Подготовка последовательного ввода
    inputs = ["100", "кг", "г"]
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter))

    # Запуск main
    main()

    # Захват вывода
    captured = capsys.readouterr().out

    # Проверка: вывод содержит числа и единицы
    assert "100" in captured
    assert "100000" in captured
    assert "кг" in captured
    assert "г" in captured
