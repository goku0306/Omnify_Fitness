from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer, String, Text, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from DBAccess.dbAccess import Base
import datetime
from Models import *

# Used To Create Class for Instructor Table
class Instructor(Base):
    __tablename__ = 'Instructor'

    InstructorID = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    InstructorName = Column(String(200), unique=True, index=True, nullable=False)
    InstructorDesc = Column(Text)
    ClassTypeID = Column(BigInteger,ForeignKey("ClassType.ClassTypeID",name='fk_Instructor_ClassTypeID'),nullable=False)
    CreatedBy = Column(BigInteger, nullable=True)
    CreatedOn = Column(DateTime, default=datetime.datetime.now, nullable=True)
    LastModifiedBy = Column(BigInteger, nullable=True)
    LastModifiedOn = Column(DateTime, nullable=True)
    InstructorStatus = Column(Integer, default=0, nullable=False)
    PrimaryKeyConstraint('InstructorID', name='pk_Instructor_InstructorID')

    ClassType = relationship('ClassType',back_populates='Instructor')
    FitnessClass = relationship('FitnessClass',back_populates='Instructor')
    