from .base import StringCondition


class StringContains(StringCondition):
    def __call__(self, val: str) -> bool:
        if not super().__call__(val):
            return False
        if self.case_insensitive:
            return self.value.lower() in val.lower()
        return self.value in val
