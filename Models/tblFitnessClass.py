from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer, String, Text, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from DBAccess.dbAccess import Base
import datetime
from Models import *

# Used To Create Class for FitnessClass Table
class FitnessClass(Base):
    __tablename__ = 'FitnessClass'

    FitnessClassID = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    FitnessClassName = Column(String(200), unique=True, index=True, nullable=False)
    ClassTypeID = Column(BigInteger,ForeignKey("ClassType.ClassTypeID",name='fk_FitnessClass_ClassTypeID'),nullable=False)
    InstructorID = Column(BigInteger,ForeignKey("Instructor.InstructorID",name='fk_FitnessClass_InstructorID'),nullable=False)
    ClassTime = Column(DateTime, nullable=False)
    TotalSlots = Column(Integer,nullable=False)
    AvailbleSlots = Column(Integer,nullable=False)
    CreatedBy = Column(BigInteger, nullable=True)
    CreatedOn = Column(DateTime, default=datetime.datetime.now, nullable=True)
    LastModifiedBy = Column(BigInteger, nullable=True)
    LastModifiedOn = Column(DateTime, nullable=True)
    FitnessClassStatus = Column(Integer, default=0, nullable=False)
    PrimaryKeyConstraint('FitnessClassID', name='pk_FitnessClass_FitnessClassID')

    ClassType = relationship('ClassType',back_populates='FitnessClass')
    Instructor = relationship('Instructor',back_populates='FitnessClass')
    ClassBooking = relationship('ClassBooking',back_populates='FitnessClass')
    