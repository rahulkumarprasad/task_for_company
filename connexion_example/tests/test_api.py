import requests
from connexion_example.database import Student, StudentSchema, session
import json

host, port=("localhost",8000)

URL="http://"+str(host)+":"+str(port)+"/"
headers={"Content-Type":"application/json"}


def test_get_all():
    global URL
    url=URL
    url+="student"
    response=requests.get(url=url,headers=headers)
    assert response.status_code==200

def test_get_one():
    global URL
    url=URL
    sample=session.query(Student).filter_by().first()
    url+="student/"+str(sample.Id)
    response=requests.get(url=url,headers=headers)
    assert response.status_code==200
    
def test_post():
    global URL
    data={'Type': 'new user', 'Description': 'my name is new user', 'Age': 100, 'Name': 'new user', 'Checked': True}
    url=URL
    url+="student"
    response=requests.post(url=url,data=json.dumps(data),headers=headers)
    assert response.status_code==201

def test_put():
    global URL
    data={'Type': 'Changing user', 'Description': 'my name is Changing user', 'Age': 10, 'Name': 'new user', 'Checked': False}
    sample=session.query(Student).filter_by().first()
    url=URL
    url+="student/"+str(sample.Id)
    response=requests.put(url=url,data=json.dumps(data),headers=headers)
    assert response.status_code==200

def test_delete():
    global URL
    sample=session.query(Student).filter_by().first()
    url=URL
    url+="student/"+str(sample.Id)
    response=requests.delete(url=url)
    assert response.status_code==204
