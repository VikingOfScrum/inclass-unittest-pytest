from wordcount import wordsInString
import pytest
#using pytest to test wordcount
@pytest.mark.parametrize("sentence, count", [
    ('hello world', 2),
    ('Today is going to be the day', 7),
    ('it is very nice outside', 5),
    ('Sometimes I wonder', 3)
])

def test_loop_for_wordcount(sentence, count):
    result = wordsInString(sentence)
    assert result == count

@pytest.mark.parametrize("sent, notcount", [
    ('The red clown wore red shoes', 4),
    ('How do we reach these kids', 5),
    ('a dog once barked', 3),
    ('Its time for a nap I think', 16)
])

def test_loop_for_not_equal(sent, notcount):
    result = wordsInString(sent)
    assert result != notcount