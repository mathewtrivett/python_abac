from typing import Union
from .base import NumericCondition


class GreaterThan(NumericCondition):
    def __call__(self, val: Union[int, float]) -> bool:
        return val > self.value


class GreaterThanOrEqual(NumericCondition):
    def __call__(self, val: Union[int, float]) -> bool:
        return val >= self.value
