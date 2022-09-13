import pytest
from python_abac.functions.numeric import (
    Equal,
    NotEqual,
    GreaterThan,
    GreaterThanOrEqual,
    LessThan,
    LessThanOrEqual,
)


class TestNumericConditionEvaluation:
    @pytest.mark.parametrize(
        "condition,value,result",
        [
            (Equal(10), 10, True),
            (Equal(10), 10.00000, True),
            (Equal(10), 11, False),
            (Equal(10.00001), 10, False),
            (NotEqual(10), 11, True),
            (NotEqual(10), 10.00001, True),
            (GreaterThan(10), 12, True),
            (GreaterThan(10), 1, False),
            (GreaterThan(10), 10.0001, True),
            (GreaterThan(10.0002), 10.0001, False),
            (GreaterThanOrEqual(10), 12, True),
            (GreaterThanOrEqual(10), 10, True),
            (GreaterThanOrEqual(10), 10.0001, True),
            (GreaterThanOrEqual(10.0002), 10.0001, False),
            (GreaterThanOrEqual(10.0002), 10.0002, True),
        ],
    )
    def test_evaluates_correctly(self, condition, value, result):
        assert condition(value) == result
