from palindrome import palindrome
import pytest
#using pytest to test palindrome
@pytest.mark.parametrize("word, expect", [
    ('uWu', True),
    ('dad', True),
    ('mom', True),
    ('SAIPPUAKIVIKAUPPIAS', True),
    ('dockers', False),
    ('choice', False),
    ('doggo', False),
    ('mississippi', False),
    ('evil live', True),
    ('I did did I', True),
    ('murder redrum', True),
    ('not today ton', False),
    ('happy birday', False)
])

def test_loop_for_palindrome(word, expect):
    result = palindrome(word)
    assert result == expect