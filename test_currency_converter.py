from currency_converter import update_cache_file
from currency_converter import calculate_amount
from currency_converter import get_exchange_rate
import pytest

def test_update_cache_file():
  assert update_cache_file("rates.json", "USD", "AED") == {"base_code": "USD", "target_code": "AED", "conversion_rate": 3.6725}
  with pytest.raises(ValueError) as sample:
    assert update_cache_file("rates.json", "USD", "KSH")


def test_calculate_amount():
  assert calculate_amount({
        "base_code": "USD",
        "target_code": "AED",
        "conversion_rate": 3.6725
    }, 5000) == "Amount in AED is 18362.50"

def test_get_exchange_rate():
  with pytest.raises(ValueError) as sample:
    assert get_exchange_rate("USD", "TSH", 5000)
