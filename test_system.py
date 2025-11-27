import pytest
from mass_converter import main

def test_system_like(monkeypatch, capsys):
    inputs = ["2", "кг", "г"]
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_iter))

    main()

    captured = capsys.readouterr().out

    # Проверка ключевых чисел и единиц
    assert "2" in captured
    assert "2000" in captured
    assert "кг" in captured
    assert "г" in captured
