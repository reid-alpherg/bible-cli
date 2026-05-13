import pytest

from bible_cli.utils import get_superscript_number


@pytest.mark.parametrize(
    ('input_value', 'expected'),
    [
        ('125', '¹²⁵'),
        (456, '⁴⁵⁶'),
        ('a1b2', 'a¹b²'),
        (3.15, '³.¹⁵'),
    ],
)
def test_get_superscript_number(input_value, expected):
    assert get_superscript_number(input_value) == expected
