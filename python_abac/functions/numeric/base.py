from dataclasses import dataclass
from typing import Union
from ..base_auth_function import BaseAuthFunction


@dataclass
class NumericCondition(BaseAuthFunction):
    value: Union[int, float]
