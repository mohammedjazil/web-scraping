from urllib.parse import quote_plus
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class wagon_mart(Base):
    __tablename__ = "grand_fresh"
    id = Column(Integer, primary_key=True)
    names = Column(String(10))
    quantity = Column(Integer)
    price = Column(Integer)
    CATEGORIES = Column(String(255))

    def __repr__(self):
        return f"({self.id}), {self.names} ,{self.price} ,{self.quantity},({self.CATEGORIES})"

username = "jazil_usr"
password = "Jazil@1233"
encoded_password = quote_plus(password)
engine = create_engine(f"mysql+pymysql://{username}:{encoded_password}@localhost/datas")

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# Query to retrieve items with stock less than 100
items_low_stock = session.query(wagon_mart).filter(wagon_mart.quantity < 100).all()

# Print the results
for item in items_low_stock:
    print(item)
