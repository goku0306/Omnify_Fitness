from sqlalchemy.orm import Session
from sqlalchemy import func
from NonEntities.FitnessClassModel import FitnessClassResponse,FitnessClasses,BookClass,BookClassResponse,ClassBookings,ClassBookingsResponse
from datetime import datetime
from Models import tblClassBooking,tblFitnessClass,tblClassType,tblInstructor

#fetch all class details
def get_all_classes(db: Session):
    try:
        all_classes = db.query(tblFitnessClass.FitnessClass).filter(tblFitnessClass.FitnessClass.ClassTime>=datetime.now()).all()

        lst_classes = []
        if(len(all_classes)>0):
            lst_classes = [FitnessClasses(
                FitnessClassID=fitnessClass.FitnessClassID,
                InstructorID=fitnessClass.InstructorID,
                Instructor=db.query(tblInstructor.Instructor).filter(tblInstructor.Instructor.InstructorID==fitnessClass.InstructorID).first().InstructorName,
                ClassTypeID=fitnessClass.ClassTypeID,
                ClassType=db.query(tblClassType.ClassType).filter(tblClassType.ClassType.ClassTypeID==fitnessClass.ClassTypeID).first().ClassTypeName,
                ClassDateTime=fitnessClass.ClassTime,
                TotalSlots=fitnessClass.TotalSlots,
                AvailbleSlots=fitnessClass.AvailbleSlots,
            )
            for fitnessClass in all_classes]

        if(len(lst_classes) == 0):
            return FitnessClassResponse(
                ResponseCode=1,
                ResponseMessage="No Fitness classes found",
                data=None,
                ErrorDetails=None
            )
        
        return FitnessClassResponse(
            ResponseCode=2,
            ResponseMessage="Retrived Fitness classes",
            data=lst_classes,
            ErrorDetails=None
        )
        
    except Exception as e:
        return FitnessClassResponse(
            ResponseCode=0,
            ResponseMessage="Failed to fetch Fitness classes.",
            ErrorDetails=str(e),
            data=[]
        )
    

# To book a class
def book_class(objBookClass:BookClass,db:Session):
    try:
        objClass = db.query(tblFitnessClass.FitnessClass).filter(tblFitnessClass.FitnessClass.FitnessClassID==objBookClass.ClassID, tblFitnessClass.FitnessClass.ClassTime>datetime.now()).first()
        if(objClass==None):
            return BookClassResponse(
            ResponseCode=1,
            ResponseMessage=f'No class found for class ID {objBookClass.ClassID}',
            ErrorDetails=None,
            data=None
        )
        if(objClass.AvailbleSlots==0):
             return BookClassResponse(
            ResponseCode=1,
            ResponseMessage = f"No available slots. The class '{objClass.FitnessClassName}' is fully booked.",
            ErrorDetails=None,
            data=None
            )
        objEmail = db.query(tblClassBooking.ClassBooking).filter(tblClassBooking.ClassBooking.ClientEmail==objBookClass.Email,tblClassBooking.ClassBooking.ClassBookingID==objBookClass.ClassID).first()
        if(objEmail):
             return BookClassResponse(
            ResponseCode=1,
            ResponseMessage = f"Email {objBookClass.Email} is already registered for this class",
            ErrorDetails=None,
            data=[]
            )
        new_class = tblClassBooking.ClassBooking(
            ClientName = objBookClass.Name,
            ClientEmail = objBookClass.Email,
            FitnessClassID= objBookClass.ClassID
        )

        db.add(new_class)
        db.commit()

        objClass.AvailbleSlots = objClass.AvailbleSlots-1
        objClass.LastModifiedBy = 1
        objClass.LastModifiedOn = datetime.now()

        db.commit()

        return BookClassResponse(
            ResponseCode=2,
            ResponseMessage="Class Booked",
            data=objBookClass,
            ErrorDetails=None
        )

    except Exception as e:
        return BookClassResponse(
            ResponseCode=0,
            ResponseMessage="Failed while booking a class.",
            ErrorDetails=str(e),
            data=[]
        )


# To get booking for specific email 
def get_bookings(email:str,db:Session):
    try:
        all_bookings = db.query(tblClassBooking.ClassBooking).filter(tblClassBooking.ClassBooking.ClientEmail==email).all()
        if(len(all_bookings)==0):
            return ClassBookingsResponse(
            ResponseCode=1,
            ResponseMessage=f"No booking found for Email ID {email}",
            ErrorDetails=None,
            data=None
            )
        lst_bookings = [
            ClassBookings(
                FitnessClassID=fitnessClass.FitnessClassID,
                InstructorID=db.query(tblFitnessClass.FitnessClass).filter(tblFitnessClass.FitnessClass.FitnessClassID==fitnessClass.FitnessClassID).first().InstructorID,
                ClassTypeID=db.query(tblFitnessClass.FitnessClass).filter(tblFitnessClass.FitnessClass.FitnessClassID==fitnessClass.FitnessClassID).first().ClassTypeID,
                ClassDateTime=db.query(tblFitnessClass.FitnessClass).filter(tblFitnessClass.FitnessClass.FitnessClassID==fitnessClass.FitnessClassID).first().ClassTime,
            )
        for fitnessClass in all_bookings]

        return ClassBookingsResponse(
             ResponseCode=2,
            ResponseMessage="Successfully retrived bookings.",
            ErrorDetails=None,
            data=lst_bookings
        )
    except Exception as e:
        return ClassBookingsResponse(
            ResponseCode=0,
            ResponseMessage="Failed to retrive booking classes.",
            ErrorDetails=str(e),
            data=None
        )