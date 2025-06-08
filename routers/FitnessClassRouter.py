from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Models import *
from NonEntities import FitnessClassModel
from repository import FitnessClassRepo
from DBAccess.dbAccess import get_db
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/Fitness",
    tags=["Fitness Class Booking"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}}
)

# Get All classess endpoint
@router.get("/classes", response_model=FitnessClassModel.FitnessClassResponse)
def get_classes( db: Session = Depends(get_db)):
    try:
        db_classes = FitnessClassRepo.get_all_classes(db=db)
        if db_classes is None:
            return JSONResponse(
                status_code=412,
                content=FitnessClassModel.FitnessClassResponse(
                    ResponseCode=2,
                    ResponseMessage="No Fitness classes found",
                    ErrorDetails="",
                    data=None
                )
            )
        return db_classes
    except Exception as ex:
        return JSONResponse(
            status_code=500,
            content=FitnessClassModel.FitnessClassResponse(
                ResponseCode=0,
                ResponseMessage="Error while fetching Fitness classes.",
                ErrorDetails=str(ex),
                data=None
            )
        )

# Book class Endpoint
@router.post("/book", response_model=FitnessClassModel.BookClassResponse)
def book_class( objClass:FitnessClassModel.BookClass,db: Session = Depends(get_db)):
    try:
        book_class = FitnessClassRepo.book_class(objClass,db=db)
        if book_class is None:
            return JSONResponse(
                status_code=412,
                content=FitnessClassModel.BookClassResponse(
                    ResponseCode=2,
                    ResponseMessage="Error while booking a class",
                    ErrorDetails="",
                    data=None
                )
            )
        return book_class
    except Exception as ex:
        return JSONResponse(
            status_code=500,
            content=FitnessClassModel.BookClassResponse(
                ResponseCode=0,
                ResponseMessage="Error while booking a Fitness classes.",
                ErrorDetails=str(ex),
                data=None
            )
        )


# Get All classess endpoint
@router.get("/bookings/{email}", response_model=FitnessClassModel.ClassBookingsResponse)
def class_bookings(email:str, db: Session = Depends(get_db)):
    try:
        db_bookings = FitnessClassRepo.get_bookings(email,db=db)
        if db_bookings is None:
            return JSONResponse(
                status_code=412,
                content=FitnessClassModel.ClassBookingsResponse(
                    ResponseCode=2,
                    ResponseMessage="No bookings found",
                    ErrorDetails="",
                    data=None
                )
            )
        return db_bookings
    except Exception as ex:
        return JSONResponse(
            status_code=500,
            content=FitnessClassModel.ClassBookingsResponse(
                ResponseCode=0,
                ResponseMessage="Error while fetching bookings.",
                ErrorDetails=str(ex),
                data=None
            )
        )
