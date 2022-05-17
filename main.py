from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://pbbot_kakxochesh:U_9J29tz~k@pbbot.mysql.tools/pbbot_kakxochesh', echo=False)

Base = declarative_base()


class Car(Base):
    __tablename__ = 'Cars'

    id_car = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    firm_id = Column(Integer, ForeignKey('Firms.id_firm'))
    price = Column(Integer, nullable=False)
    Firm = relationship('Firm')


class Firm(Base):
    __tablename__ = 'Firms'

    id_firm = Column(Integer, primary_key=True)
    firm_name = Column(String(250), nullable=False)
    car = relationship('Car')


Base.metadata.create_all(engine)
