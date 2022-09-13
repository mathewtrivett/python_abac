from .base import StringCondition


class StringEqual(StringCondition):
    def __call__(self, val: str) -> bool:
        if not super().__call__(val):
            return False
        if self.case_insensitive:
            return val.lower() == self.value.lower()
        return val == self.value


class StringNotEqual(StringCondition):
    def __call__(self, val: str) -> bool:
        if not super().__call__(val):
            return False
        if self.case_insensitive:
            return val.lower() != self.value.lower()
        return val != self.value
