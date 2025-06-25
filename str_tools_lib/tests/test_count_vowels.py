from ..operations import count_vowels


class TestCountVowels:
    """Tests for 'count_vowels' function"""

    def test_count_vowels_normal_word(self):
        """Normal english words count vowels test"""
        assert count_vowels('hello world') == 3

    def test_count_vowels_mixed_case(self):
        """Mixed case count vowels test"""
        assert count_vowels('AEIOUYaeiouy') == 12

    def test_count_vowels_no_vowels(self):
        """No vowels string test"""
        assert count_vowels('123/*-#$') == 0
