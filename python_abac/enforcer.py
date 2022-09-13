from typing import Tuple
from .request import Request
from .response import Response


class Enforcer:
    """
    AuthorisationEnforcer is the Policy Enforcement Point in python_abac.
    It is responsible for making an AuthorisationRequest to
    the AuthorisationDecider and acting on the AuthorisationResponse.
    """

    def __init__(self, decision_service):
        self.decision_service = decision_service

    async def is_authorised(self, auth_request: Request) -> Tuple[bool, Response]:
        response = await self.decision_service.evaluate(auth_request)
        return response.is_allowed(), response
