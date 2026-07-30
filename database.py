from sqlalchemy import create_engine
#to create connection with database
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/mobiles_db"
DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_wjN3XLOMbXUa5Dqz1h0@mysql-15560c42-mpavani596-a3aa.j.aivencloud.com:24476/defaultdb"

engine = create_engine(DATABASE_URL, connect_args={"ssl":{}} )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
