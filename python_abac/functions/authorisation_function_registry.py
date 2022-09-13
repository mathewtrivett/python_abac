from typing import Callable
from dataclasses import dataclass, field


class AuthFunctionOverrideError(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AuthFunctionNotCallable(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


@dataclass
class AuthorisationFunctionRegistry:
    """
    The AuthorisationFunctionRegistry allows registration and fetching of registration function callables.
    """

    __register: dict[str, Callable] = field(default_factory=dict, init=False)

    @property
    def all(self):
        return self.__register

    def register(self, identifier: str, func: Callable, replace: bool = False):
        if not callable(func):
            raise AuthFunctionNotCallable("Auth function must be a callable object")
        if self.__register.get(identifier) and not replace:
            raise AuthFunctionOverrideError(
                f"""
                Callable exists with identifier `{identifier}`. 
                Use a different identifier or override the 
                implementation by passing in `replace=True`"""
            )
        else:
            self.__register = dict(self.__register, **{identifier: func})
        return self.__register

    def get(self, identifier: str):
        return self.__register[identifier]
