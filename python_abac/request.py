from pydantic import BaseModel


class Request(BaseModel):
    """
    An AuthorisationRequest is a structured way of making an
    access request for a specific resource.
    """

    ReturnPolicyIdList: bool = False
    CombinedDecision: bool = False

    AccessSubject: dict
    Action: dict
    Resource: dict
