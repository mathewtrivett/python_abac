from unittest.mock import MagicMock, AsyncMock
import pytest
from python_abac import Enforcer, Response, Decision


@pytest.mark.asyncio
class TestAuthorisationEnforcer:
    @pytest.fixture
    def truthy_response(self):
        """
        Constructs a Permit response
        """
        return Response(Decision.Permit)

    @pytest.fixture
    def falsy_response(self):
        """
        Constructs a Denied response
        """
        return Response(Decision.Deny)

    @pytest.fixture
    def mock_decision_service(self):
        """
        Create a mock decision service. Allow the return value
        to be overridden.
        """
        pass

    @pytest.mark.parametrize(
        "decision_service,response,allowed", [(truthy_response), (falsy_response)]
    )
    async def test_correctly_enforces_decision(
        self, decision_service, response, allowed
    ):
        enforcer = Enforcer(decision_service=decision_service)
        allow, res = await enforcer.is_authorised(auth_request={})
        assert res == response
        assert allow == allowed
