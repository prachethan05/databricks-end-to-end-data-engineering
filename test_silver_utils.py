import pytest

from silver_utils import validate_dataset_name


def test_valid_name_is_returned():
    assert validate_dataset_name("google_ads_campaigns") == "google_ads_campaigns"


def test_spaces_and_capitals_are_cleaned():
    assert validate_dataset_name("  Google_Ads  ") == "google_ads"


def test_empty_name_raises_error():
    with pytest.raises(ValueError):
        validate_dataset_name("")


def test_name_starting_with_digit_raises_error():
    with pytest.raises(ValueError):
        validate_dataset_name("1_sales")


def test_name_with_dash_raises_error():
    with pytest.raises(ValueError):
        validate_dataset_name("sales-data")