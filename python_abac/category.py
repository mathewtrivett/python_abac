from enum import Enum
from pydantic import BaseModel


class CategoryIdEnum(str, Enum):
    Resource = "urn:oasis:names:tc:xacml:3.0:attribute-category:resource"
    Action = "urn:oasis:names:tc:xacml:3.0:attribute-category:action"
    Environment = "urn:oasis:names:tc:xacml:3.0:attribute-category:environment"
    AccessSubject = "urn:oasis:names:tc:xacml:1.0:subject-category:access-subject"
    RecipientSubject = "urn:oasis:names:tc:xacml:1.0:subject-category:recipient-subject"
    IntermediarySubject = (
        "urn:oasis:names:tc:xacml:1.0:subject-category:intermediary-subject"
    )
    Codebase = "urn:oasis:names:tc:xacml:1.0:subject-category:codebase"
    RequestingMachine = (
        "urn:oasis:names:tc:xacml:1.0:subject-category:requesting-machine"
    )


class Category(BaseModel):
    CategoryId: CategoryIdEnum
    Id: str = None
    Content: str = None
