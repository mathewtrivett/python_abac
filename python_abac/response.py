from enum import Enum
from pydantic import BaseModel


class DecisionEnum(str, Enum):
    Permit = "Permit"
    Deny = "Deny"
    NotApplicable = "NotApplicable"
    Indeterminate = "Indeterminate"


class Response(BaseModel):
    """
    An AuthorisationResponse is a formal response to an AuthorisationRequest.
    AuthorisationResponses are emitted by the AuthorisationDecider.
    """

    Decision: DecisionEnum

    def is_allowed(self):
        return self.Decision == DecisionEnum.Permit
