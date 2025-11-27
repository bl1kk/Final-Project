import pytest
from mass_converter import convert_mass

def test_convert_mass_basic():
    assert convert_mass(1, "кг", "г") == pytest.approx(1000.0)
    assert convert_mass(1, "г", "кг") == pytest.approx(0.001)

def test_convert_mass_aliases():
    assert convert_mass(1, "lb", "фунт") == pytest.approx(1.0)
    assert convert_mass(16, "oz", "фунт") == pytest.approx(1.0)

def test_convert_mass_unknown_unit():
    with pytest.raises(ValueError):
        convert_mass(1, "unknown", "кг")
    with pytest.raises(ValueError):
        convert_mass(1, "кг", "unknown")

def test_convert_mass_edge_cases():
    assert convert_mass(0, "кг", "г") == 0
    assert convert_mass(1e6, "г", "т") == pytest.approx(1.0)
