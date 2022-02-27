from database import Student, StudentSchema, session
import json
from flask import request


def get_student():
    # do something
    stu_obj = session.query(Student).all()
    stu_sch = StudentSchema(many=True)
    dat = stu_sch.dumps(stu_obj)
    return dat, 200

def post_student():
    # do something
    new_obj=Student()
    stu_sch = StudentSchema()
    data=json.loads(request.data)
    for key, value in data.items():
        setattr(new_obj, key, value)

    session.add(new_obj)
    session.commit()
    dat = stu_sch.dumps(new_obj)
    return dat, 201

def get_student_detail(student_id):
    try:
        stu_obj = session.query(Student).filter_by(Id=student_id).first()
        stu_sch = StudentSchema()
        dat = stu_sch.dumps(stu_obj)
        print(request)
        return dat, 200
    except:
        return "Not Found",404

def update_student(student_id):
    stu_obj = session.query(Student).filter_by(Id=student_id).first()
    try:
        stu_sch = StudentSchema()
        up_data = json.loads(request.data)
        print(up_data)
        #stmt = (update(Student).where(Student.Id == student_id).values(up_data))
        for key, value in up_data.items():
            setattr(stu_obj, key, value)
        
        session.commit()
        response=stu_sch.dumps(stu_obj)
        return response, 200
    except:
        return "Not Found",404

def delete_student(student_id):
    try:
        stmt= session.query(Student).filter_by(Id=student_id).delete()
        session.commit()
        return stmt, 204
    except:
        return "Not Found",404