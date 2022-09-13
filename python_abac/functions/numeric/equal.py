from typing import Union
from .base import NumericCondition


class Equal(NumericCondition):
    def __call__(self, val: Union[int, float]) -> bool:
        return val == self.value


class NotEqual(NumericCondition):
    def __call__(self, val: Union[int, float]) -> bool:
        return val != self.value
