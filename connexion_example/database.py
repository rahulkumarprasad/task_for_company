import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import datetime

engine = sa.create_engine("sqlite:///database.db")
session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    Id = sa.Column(sa.Integer, primary_key=True)
    Checked = sa.Column(sa.Boolean, nullable=False)
    Name = sa.Column(sa.String, nullable=False)
    Type = sa.Column(sa.String, nullable=False)
    Age = sa.Column(sa.Integer, nullable=False)
    Description = sa.Column(sa.String, nullable=False)
    Date = sa.Column(sa.DateTime, default=datetime.datetime.now)


    def __repr__(self):
        return "<Student(name={self.Name!r})>".format(self=self)


Base.metadata.create_all(engine)



class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        load_instance = True


def insert_sample_data():
    all_student = [{"Checked":True,"Name":"test1","Type":"test1","Age":25,"Description":"my name is test1"},{"Checked":True,"Name":"test2","Type":"test2","Age":28,"Description":"my name is test2"},{"Checked":True,"Name":"test3","Type":"test3","Age":20,"Description":"my name is test3"},{"Checked":True,"Name":"test4","Type":"test4","Age":18,"Description":"my name is test4"}]
    for data in all_student:
        obj=Student(Checked=data["Checked"],Name=data["Name"],Type=data["Type"],Age=data["Age"],Description=data["Description"])
        session.add(obj)
        session.commit()

insert_sample_data()