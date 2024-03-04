from urllib.parse import quote_plus
from sqlalchemy import create_engine ,Column,String,Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class stor(Base):
    __tablename__ = "table"
    id= Column(Integer, primary_key=True)
    name=Column(String(10))
    quantity =Column(Integer)
    price=Column(Integer)
    category = Column(String(255))

    # def __repr__(self):
    #     return f"({self.id}), {self.name} ,{self.price},{self.quantity} ,({self.age})"

username = "jazil_usr"
password = "Jazil@1233"
encoded_password = quote_plus(password)
engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@localhost/store")

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# new_store =stor(name='orange',quantity=10,price=3,category='fruits')
# session.add(new_store)
# session.commit

# market = session.query(stor).all()
# for i in market:
#     print(i.id,i.name,i.quantity,i.price,i.category)

vegetables = session.query(stor).filter_by(category='friuts').all()

for i in vegetables:
    print(i)
