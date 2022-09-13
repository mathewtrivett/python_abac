from .base import StringCondition


class StringEndsWith(StringCondition):
    def __call__(self, val: str) -> bool:
        if not super().__call__(val):
            return False
        if self.case_insensitive:
            return val.lower().endswith(self.value.lower())
        return val.endswith(self.value)
