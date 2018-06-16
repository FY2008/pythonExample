from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, String, Integer, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship
import psycopg2


engine = create_engine(
        'postgresql+psycopg2://testUser:testpassword@192.168.1.122:5432/ormdb4')
Session = sessionmaker(bind=engine)

Base = declarative_base()


# 中间表
teacher_classes = Table(
        'teacher_classes',
        Base.metadata,
        Column('teacher_id', Integer, ForeignKey('teacher.id'), nullable=False, primary_key=True),
        Column('classes_id', Integer, ForeignKey('classes.id'), nullable=False, primary_key=True))


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_name = Column(String(100))
    classes = relationship('Classes', secondary=teacher_classes)

    def __repr__(self):
        return "<Teacher id='%s' teacher_name='%s'>" % (self.id, self.teacher_name)

class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    classes_name = Column(String(100))
    teacher = relationship('Teacher', secondary=teacher_classes)

    def __repr__(self):
        return "<Classes id='%s' Classes_name='%s'" % (self.id, self.classes_name)
