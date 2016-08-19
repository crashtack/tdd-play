# -*- coding: utf-8 -*-
import pytest

ACK_TABLE = [
    (0, 0, 1),
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 5),
    (1, 0, 2),
    (1, 1, 3),
    (1, 2, 4),
    (1, 3, 5),
    (1, 4, 6),
    (2, 0, 3),
    (2, 1, 5),
    (2, 2, 7),
    (2, 3, 9),
    (2, 4, 11),
    (3, 0, 5),
    (3, 1, 13),
    (3, 2, 29),
    (3, 3, 61),
    (3, 4, 125)
]
BAD_TABLE = [
    ('a', 'b'),
    (-1, 'c'),
    (-1, 1),
    ('c', 1)
]


@pytest.mark.parametrize('m, n, result', ACK_TABLE)
def test_akermann(m, n, result):
    from ackermann import ackermann
    assert ackermann(m, n) == result


@pytest.mark.parametrize('m, n', BAD_TABLE)
def test_bad_inputs(m, n):
    from ackermann import ackermann
    with pytest.raises(ValueError):
        ackermann(m, n)
