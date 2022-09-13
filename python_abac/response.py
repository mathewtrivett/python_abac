from enum import Enum
from pydantic import BaseModel


class Decision(str, Enum):
    Permit = "Permit"
    Deny = "Deny"
    NotApplicable = "NotApplicable"
    Indeterminate = "Indeterminate"


class Response(BaseModel):
    """
    An AuthorisationResponse is a formal response to an AuthorisationRequest.
    AuthorisationResponses are emitted by the AuthorisationDecider.
    """

    Decision: Decision

    def is_allowed(self):
        return self.Decision == Decision.Permit
