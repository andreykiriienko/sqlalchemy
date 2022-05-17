import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Car, Firm

pymysql.install_as_MySQLdb()

engine = create_engine('mysql+pymysql://pbbot_kakxochesh:U_9J29tz~k@pbbot.mysql.tools/pbbot_kakxochesh', echo=True)

session = sessionmaker(bind=engine)


def create_car(name, firm_id, price):
    sess = session()
    car_one = Car(name=name, firm_id=firm_id, price=price)

    sess.add(car_one)
    sess.commit()
    sess.close()


def create_firm(id_firm, firm_name, car):
    sess = session()
    car_one = Firm(id_firm=id_firm, firm_name=firm_name, car=car)

    sess.add(car_one)
    sess.commit()
    sess.close()


create_car('BMW', 2, 4000)
