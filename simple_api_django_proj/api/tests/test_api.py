import pytest
from django.urls import reverse ,resolve
from rest_framework.reverse import reverse as reverse_rest
import requests
from django.test import Client
from api.models import TaskModel
from django.contrib.auth.models import User
import json
from django.test import TestCase


class TestApi(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestApi,cls).setUpClass()
        insert_sample_data()
        cls.client=Client()
        url = reverse("token_obtain_pair")
        data = cls.client.post(url,data={"username":"admin","password":"Qwertyuiop@123"})
        cls.token=json.loads(data.content)
        cls.header={'HTTP_AUTHORIZATION': f"Bearer {cls.token['access']}","content_type":"application/json"}

    def test_get(self):
        url=reverse_rest("student-list")
        total_stu = TaskModel.objects.all().count()
        res=self.client.get(url,**self.header)
        data = json.loads(res.content)
        assert total_stu==len(data)

    def test_get_second(self):
        url=reverse_rest("student-list")
        view_cls = resolve(url).func.__name__
        assert view_cls=="TestApi"


    def test_post(self):
        url=reverse_rest("student-list")
        data={"Checked":True,"Name":"rahul","Type":"rahul","Age":50,"Description":"my name is rahul"}
        res=self.client.post(url,data=data,**self.header)
        assert res.status_code==201

    def test_post_second(self):
        url=reverse_rest("student-list")
        view_cls = resolve(url).func.__name__
        assert view_cls=="TestApi"

    def test_get_one_data(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all()[0]
        url=url+str(f"{test_stu.Id}/")
        res=self.client.get(url,**self.header)
        data = json.loads(res.content)
        assert data["Id"]==test_stu.Id

    def test_get_one_data_second(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all()[0]
        url=url+str(f"{test_stu.Id}/")
        res=self.client.get(url,**self.header)
        data = json.loads(res.content)
        assert data["Checked"]==test_stu.Checked
        assert data["Name"]==test_stu.Name
    
    def test_put(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all().values("Id","Checked","Name","Type","Age","Description")[0]
        test_stu["Name"]="sonu"
        test_stu["Checked"]=False
        test_stu["Age"]=100
        url=url+str(f"{test_stu['Id']}/")
        test_stu.pop("Id")
        res=self.client.put(url,data=test_stu,**self.header)
        data = json.loads(res.content)
        assert res.status_code==200

    def test_put_second(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all().values("Id","Checked","Name","Type","Age","Description")[0]
        test_stu["Name"]="sonu"
        test_stu["Checked"]=False
        test_stu["Age"]=100
        url=url+str(f"{test_stu['Id']}/")
        test_stu.pop("Id")
        res=self.client.put(url,data=test_stu,**self.header)
        data = json.loads(res.content)
        assert  test_stu["Name"]==data["Name"]
        assert  test_stu["Age"]==data["Age"]
        assert  test_stu["Checked"]==data["Checked"]
    
    def test_put_second(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all().values("Id","Checked","Name","Type","Age","Description")[0]
        test_stu["Name"]="sonu"
        test_stu["Checked"]=False
        test_stu["Age"]=100
        url=url+str(f"{test_stu['Id']}/")
        test_stu.pop("Id")
        res=self.client.put(url,data=test_stu,**self.header)
        data = json.loads(res.content)
        assert  test_stu["Name"]==data["Name"]
        assert  test_stu["Age"]==data["Age"]
        assert  test_stu["Checked"]==data["Checked"]

    def test_patch(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all().values("Id","Checked","Name","Type","Age","Description")[0]
        url=url+str(f"{test_stu['Id']}/")
        test_stu.pop("Id")
        res=self.client.patch(url,data={"Name":"sonu king","Age":10},**self.header)
        data = json.loads(res.content)
        assert  res.status_code==200

    def test_patch_second(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all().values("Id","Checked","Name","Type","Age","Description")[0]
        url=url+str(f"{test_stu['Id']}/")
        test_stu.pop("Id")
        res=self.client.patch(url,data={"Name":"sonu king","Age":10},**self.header)
        data = json.loads(res.content)
        assert  data["Name"]=="sonu king"
        assert  data["Age"]==10

    def test_delete(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all().values("Id","Checked","Name","Type","Age","Description")[0]
        url=url+str(f"{test_stu['Id']}/")
        test_stu.pop("Id")
        res=self.client.delete(url,**self.header)
        assert  res.status_code==204

    def test_delete_second(self):
        url=reverse_rest("student-list")
        test_stu=TaskModel.objects.all().values("Id","Checked","Name","Type","Age","Description")[0]
        url=url+str(f"{test_stu['Id']}/")
        id=test_stu.pop("Id")
        res=self.client.delete(url,**self.header)
        try:
            TaskModel.objects.get(Id=id)
            assert 1==2 , "The User Still exists"
        except TaskModel.DoesNotExist:
            pass

        assert  res.status_code==204

def insert_sample_data():
    all_student = [{"Checked":True,"Name":"test1","Type":"test1","Age":25,"Description":"my name is test1"},{"Checked":True,"Name":"test2","Type":"test2","Age":28,"Description":"my name is test2"},{"Checked":True,"Name":"test3","Type":"test3","Age":20,"Description":"my name is test3"},{"Checked":True,"Name":"test4","Type":"test4","Age":18,"Description":"my name is test4"}]
    for data in all_student:
        TaskModel.objects.create(Checked=data["Checked"],Name=data["Name"],Type=data["Type"],Age=data["Age"],Description=data["Description"])
    User.objects.create_user(username="admin",email="admin@gmail.com",password="Qwertyuiop@123")
