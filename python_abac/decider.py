from .attribute_store import AttributeStore
from .policy_store import PolicyStore


class Decider:
    """
    The Decider acts as the Policy Decision Point in python_abac.
    It is responsible for evaluating Requests against Policys.

    And issuing Responses back to the Enforcer.
    """

    def __init__(self, policy_store: PolicyStore, attribute_store: AttributeStore):
        self.policy_store = policy_store
        self.attribute_store = attribute_store

    async def evaluate(self, auth_request):
        pass
