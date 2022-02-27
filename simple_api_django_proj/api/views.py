from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import TestModelSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

@method_decorator(name="list",decorator=swagger_auto_schema(operation_description='GET /api/student/, List all students.'))
@method_decorator(name="create",decorator=swagger_auto_schema(operation_description='POST /api/student/, Create new student.'))
@method_decorator(name="retrieve",decorator=swagger_auto_schema(operation_description='GET /api/student/{id}/, Get detail of one student.'))
@method_decorator(name="update",decorator=swagger_auto_schema(operation_description='PUT /api/student/{id}/, Update all fields of one student.'))
@method_decorator(name="partial_update",decorator=swagger_auto_schema(operation_description='PATCH /api/student/{id}/, Make update to some fields of one student.'))
@method_decorator(name="destroy",decorator=swagger_auto_schema(operation_description='DELETE /api/student/{id}/, Delete one student.'))
class TestApi(ModelViewSet):
    serializer_class = TestModelSerializer
    queryset = TaskModel.objects.all()
    http_method_names=["get","post","put","patch","delete"]
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]