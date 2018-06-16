from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, BIGINT, Text, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
import psycopg2
engine = create_engine(
    'postgresql+psycopg2://testUser@10.10.129.116:5432/ormdb1')
ModelBase = declarative_base()  # 元类
Session = sessionmaker(bind=engine)


class User(ModelBase):
    __tablename__ = 'auth_user'
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    date_joined = Column(DateTime)
    username = Column(String(length=30), server_default='', nullable=False, index=True)
    password = Column(String(length=128), server_default='', nullable=False)

    def __repr__(self):
        return "<User(username='%r', date_joined='%r', password='%r')" % (
            self.username, self.date_joined, self.password)

class Blog(ModelBase):
    __tablename__ = 'blog'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    title = Column(String(length=120), server_default='', nullable=False)
    text = Column(Text, server_default='', nullable=True)

