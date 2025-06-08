from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel 

T = TypeVar("T")
# Generic Response Model class
class APIResponse(GenericModel, Generic[T]):
    ResponseCode: int
    ResponseMessage: str
    ErrorDetails: Optional[str] = None
    data: Optional[T] = None

