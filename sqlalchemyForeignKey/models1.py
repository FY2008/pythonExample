"""
sqlalchemy 多对一关系简单例子
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, CHAR
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import relationship,backref, sessionmaker
import psycopg2
engine = create_engine(
    'postgresql+psycopg2://testUser@10.10.129.116:5432/ormdb3')
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(50))

    def __repr__(self):
        return "<Parent: '%s'>" % self.name


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(CHAR(50))
    parent_id = Column(Integer, ForeignKey('parent.id'))
    child = relationship('Parent', backref='child')
    def __repr__(self):
        return "<Child: '%s'>" % self.name

"""
我们在关系中定义了一个backref='child'，我们可以通过child访问对方的数据
"""
