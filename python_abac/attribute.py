from typing import Union, Any
from pydantic import BaseModel


class Attribute(BaseModel):
    AttributeId: str
    Value: Any
    DataType: Union[str, None]
    IncludeInResult: bool = False
