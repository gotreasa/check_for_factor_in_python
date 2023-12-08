import pytest

from modules import factor


def describe_check_for_factor():
    def should_error_when_factor_is_negative_number():
        """🧪 should give an error if the factor is a negative number"""
        with pytest.raises(ValueError, match="❗️ Factor must be a positive integer"):
            factor.check_for_factor(8, -2)

    def should_error_when_base_is_negative_number():
        """🧪 should give an error if the base is a negative number"""
        with pytest.raises(ValueError, match="❗️ Base must be a positive integer"):
            factor.check_for_factor(-8, 2)

    def should_error_when_base_is_not_an_integer():
        """🧪 should give an error if the base is not an integer"""
        with pytest.raises(ValueError, match="❗️ Base must be a positive integer"):
            factor.check_for_factor("blah", 2)

    def should_indicate_2_is_a_factor_of_6():
        """🧪 should indicate 2 is a factor of 6"""
        assert factor.check_for_factor(6, 2)

    def should_indicate_3_is_a_factor_of_6():
        """🧪 should indicate 3 is a factor of 6"""
        assert factor.check_for_factor(6, 3)

    def should_indicate_3_is_a_factor_of_12():
        """🧪 should indicate 3 is a factor of 12"""
        assert factor.check_for_factor(12, 3)

    def should_indicate_7_is_a_factor_of_14():
        """🧪 should indicate 7 is a factor of 14"""
        assert factor.check_for_factor(14, 7)

    def should_indicate_7_is_NOT_a_factor_of_6():
        """🧪 should indicate 7 is NOT a factor of 6"""
        assert factor.check_for_factor(6, 7) == False

    def should_indicate_7_is_NOT_a_factor_of_4():
        """🧪 should indicate 7 is NOT a factor of 4"""
        assert factor.check_for_factor(4, 7) == False

    def should_indicate_3_is_NOT_a_factor_of_14():
        """🧪 should indicate 3 is NOT a factor of 14"""
        assert factor.check_for_factor(14, 3) == False

    def should_indicate_5_is_NOT_a_factor_of_12():
        """🧪 should indicate 5 is NOT a factor of 12"""
        assert factor.check_for_factor(12, 5) == False
