from dataclasses import dataclass

from ..base_auth_function import BaseAuthFunction


@dataclass
class StringCondition(BaseAuthFunction):
    value: str
    case_insensitive: bool = False

    def __call__(self, val: str) -> bool:
        return isinstance(val, str)
