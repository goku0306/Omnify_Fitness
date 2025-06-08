from typing import Optional,List
from pydantic import BaseModel
from NonEntities.responseModel import APIResponse
import datetime

# Class Model to get Classes
class FitnessClasses(BaseModel):
    FitnessClassID:int
    InstructorID:int
    Instructor:str
    ClassTypeID:int
    ClassType:str
    ClassDateTime:datetime.datetime
    TotalSlots:int
    AvailbleSlots:int

    class Config:
        orm_mode = True

# Model class to book a class
class BookClass(BaseModel):
    ClassID:int
    Name:str
    Email:str

    class Config:
        orm_mode = True

# Model class to get bookings
class ClassBookings(BaseModel):
    FitnessClassID:int
    InstructorID:int
    ClassTypeID:int
    ClassDateTime:datetime.datetime

# Response Model with model class
FitnessClassResponse = APIResponse[List[FitnessClasses]]
BookClassResponse = APIResponse[BookClass]
ClassBookingsResponse = APIResponse[List[ClassBookings]]
