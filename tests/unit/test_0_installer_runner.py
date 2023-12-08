import pytest

from modules import factor


def describe_check_for_factor():
    def should_error_when_factor_is_negative_number():
        """🧪 should give an error if the factor is a negative number"""
        with pytest.raises(ValueError, match="❗️ Factor must be a positive integer"):
            factor.check_for_factor(8, -2)
