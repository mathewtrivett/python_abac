from .base import StringCondition


class StringStartsWith(StringCondition):
    def __call__(self, val: str) -> bool:
        if not super().__call__(val):
            return False
        if self.case_insensitive:
            return val.lower().startswith(self.value.lower())
        return val.startswith(self.value)
