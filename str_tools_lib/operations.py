def reverse_string(s: str) -> str:
    """
    Returns reversed string:
    'qwerty' -> 'ytrewq'
    """
    return s[::-1]


def count_vowels(s: str) -> int:
    """
    Counts all the english vowels in the string (Caps do not matter):
    'qwerty' -> 2
    'QWErTy' -> 2
    """
    vowels = 'aeiouy'
    return sum(1 for char in s.lower() if char in vowels)


def is_palindrome(s: str) -> bool:
    """
    Checks if the string is palindrome (Caps do not matter, ignores all the chars except A-Za-z0-9):
    'qwerty' -> False
    'level'  -> True
    'LEv@el' -> True
    """
    cleaned = ''.join(char for char in s.lower() if char.isalnum())
    return cleaned == cleaned[::-1]
