from typing import Tuple
from .request import Request
from .response import Response


class Enforcer:
    """
    Enforcer is the Policy Enforcement Point in python_abac.
    It is responsible for making an Request to
    the Decider and acting on the Response.
    """

    def __init__(self, decision_service):
        self.decision_service = decision_service

    async def is_authorised(self, auth_request: Request) -> Tuple[bool, Response]:
        response = await self.__authorise(auth_request)
        return response.is_allowed(), response

    async def __authorise(self, auth_request: Request) -> Tuple[bool, Response]:
        response = await self.decision_service.evaluate(auth_request)
        return response
