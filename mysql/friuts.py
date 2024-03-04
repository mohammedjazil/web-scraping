from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class wagon_mart(Base):
    __tablename__ = "wagon_mart"
    id = Column(Integer, primary_key=True)
    names = Column(String(10))
    quantity = Column(Integer)
    price = Column(Integer)
    CATEGORIES = Column(String(255))

    def __repr__(self):
        return f"({self.id}), {self.names} ,{self.price},{self.quantity} ,({self.CATEGORIES})"

username = "jazil_usr"
password = "Jazil@1233"
encoded_password = quote_plus(password)
engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@localhost/datas")

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Filter for fruits and order by price in ascending order
cheapest_fruits = session.query(wagon_mart).filter_by(CATEGORIES='fruits').order_by(wagon_mart.price).all()

# Print the cheapest fruits
for fruit in cheapest_fruits:
    print(f"Fruit: {fruit.names}, Price: {fruit.price}")
