from typing import Union
from .base import NumericCondition


class LessThan(NumericCondition):
    def __call__(self, val: Union[int, float]) -> bool:
        return val < self.value


class LessThanOrEqual(NumericCondition):
    def __call__(self, val: Union[int, float]) -> bool:
        return val <= self.value
