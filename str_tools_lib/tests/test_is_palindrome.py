from ..operations import is_palindrome


class TestIsPalindrome:
    """Tests for 'is_palindrome' function"""

    def test_is_palindrome_ok(self):
        """Normal english palindrome test"""
        assert is_palindrome('madam') is True

    def test_is_palindrome_mixed_case_ok(self):
        """Normal english mixed case palindrome test"""
        assert is_palindrome('MADam') is True

    def test_is_palindrome_with_spaces(self):
        """English palindrome sentence with spaces test"""
        assert is_palindrome('A man a plan a canal Panama') is True

    def test_is_palindrome_with_punctuation(self):
        """English palindrome sentence with punctuation test"""
        assert is_palindrome('Was it a car, or a cat I saw?') is True

    def test_is_palindrome_empty_string(self):
        """String with special chars reverse test"""
        assert is_palindrome('') is True

    def test_is_palindrome_not_palindrome(self):
        """Normal english not palindrome word test"""
        assert is_palindrome('hello') is False
