from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer, String, Text, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from DBAccess.dbAccess import Base
import datetime
from Models import *

# Used To Create Class for ClassBooking Table
class ClassBooking(Base):
    __tablename__ = 'ClassBooking'

    ClassBookingID = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    ClientName = Column(String(250),nullable=False)
    ClientEmail = Column(String(300),nullable=False)
    FitnessClassID = Column(BigInteger,ForeignKey("FitnessClass.FitnessClassID",name='fk_ClassBooking_FitnessClassID'),nullable=False)
    CreatedBy = Column(BigInteger, nullable=True)
    CreatedOn = Column(DateTime, default=datetime.datetime.now, nullable=True)
    LastModifiedBy = Column(BigInteger, nullable=True)
    LastModifiedOn = Column(DateTime, nullable=True)
    ClassBookingStatus = Column(Integer, default=0, nullable=False)
    PrimaryKeyConstraint('ClassBookingID', name='pk_ClassBooking_ClassBookingID')

    FitnessClass = relationship('FitnessClass',back_populates='ClassBooking')
    