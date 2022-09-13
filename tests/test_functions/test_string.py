import pytest

from python_abac.functions.string import (
    StringContains,
    StringStartsWith,
    StringEndsWith,
    StringEqual,
    StringNotEqual,
)


class TestConditionEvaluation:
    @pytest.mark.parametrize(
        "condition, value, result",
        [
            (StringContains("a"), "abc", True),
            (StringContains("B", case_insensitive=True), "abc", True),
            (StringContains("B"), "abc", False),
            (StringContains("b"), "cde", False),
            (StringContains("b"), None, False),
            (StringStartsWith("w"), "woo", True),
            (StringStartsWith("W", case_insensitive=True), "woo", True),
            (StringStartsWith("whoo"), "woo", False),
            (StringEndsWith("c"), "abc", True),
            (StringEndsWith("d"), "abc", False),
            (StringEndsWith("D", case_insensitive=True), "abcd", True),
            (StringEndsWith("D"), "abcd", False),
            (StringEqual("abc"), "abc", True),
            (StringEqual("abc"), "def", False),
            (StringEqual("ABC", case_insensitive=True), "abc", True),
            (StringNotEqual("abc"), "abc", False),
            (StringNotEqual("abc"), "def", True),
            (StringNotEqual("ABC", case_insensitive=True), "abc", False),
        ],
    )
    def test_evaluates_correctly(self, condition, value, result):
        assert condition(value) == result
