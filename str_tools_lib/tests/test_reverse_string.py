from ..operations import reverse_string


class TestReverseString:
    """Tests for 'reverse_string' function"""

    def test_reverse_string_normal_word(self):
        """Normal english word reverse test"""
        assert reverse_string('hello') == 'olleh'

    def test_reverse_string_empty(self):
        """Empty string test"""
        assert reverse_string('') == ''

    def test_reverse_string_with_spaces(self):
        """Normal english words with spaces reverse test"""
        assert reverse_string('hello world') == 'dlrow olleh'

    def test_reverse_string_with_special_chars(self):
        """String with special chars reverse test"""
        assert reverse_string('123/*-#$') == '$#-*/321'
