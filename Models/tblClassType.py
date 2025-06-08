from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer, String, Text, DateTime, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from DBAccess.dbAccess import Base
import datetime
from Models import *

# Used To Create Class for ClassType Table
class ClassType(Base):
    __tablename__ = 'ClassType'

    ClassTypeID = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    ClassTypeName = Column(String(200), unique=True, index=True, nullable=False)
    ClassTypeDesc = Column(Text)
    CreatedBy = Column(BigInteger, nullable=True)
    CreatedOn = Column(DateTime, default=datetime.datetime.now, nullable=True)
    LastModifiedBy = Column(BigInteger, nullable=True)
    LastModifiedOn = Column(DateTime, nullable=True)
    ClassTypeStatus = Column(Integer, default=0, nullable=False)
    PrimaryKeyConstraint('ClassTypeID', name='pk_ClassType_ClassTypeID')

    Instructor = relationship('Instructor',back_populates='ClassType')
    FitnessClass = relationship('FitnessClass',back_populates='ClassType')