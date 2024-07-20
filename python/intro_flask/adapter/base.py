from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


url=URL.create(
    drivername="postgresql",
    username="postgres",
    password="123",
    host="localhost",
    port="34323",
    database="postgres"
)
engine = create_engine(url)
Session = sessionmaker(bind=engine)

Base = declarative_base()