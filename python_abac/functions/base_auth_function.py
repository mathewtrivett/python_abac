from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseAuthFunction(ABC):
    """
    AuthorisationFunctions are used to evaluate AuthorisationRequests agaisnt AuthorisationRules.
    """

    @property
    def name(self):
        return type(self).__name__

    @abstractmethod
    def __call__(self, *args, **kwargs) -> bool:
        """
        Define the auth function__call__ method
        """
        raise NotImplementedError
