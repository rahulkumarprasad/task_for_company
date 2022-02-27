"""simple_api_django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
#swager
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.clickjacking import xframe_options_sameorigin

schema_view = get_schema_view(
   openapi.Info(
      title="Student API",
      default_version='1',
      description="This Api is used for Creting Student, geeting information about student and listing all the student, updating student, deleting student.<h4 style='font-weight:400;'>For testing Api please visite <a href='/swagger/' target='blank'>Test Api</a></h4>",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email=settings.EMAIL_ADDRESS),
    #  license=openapi.License(name="BSD"),
   ),
   public=True,
   
)


urlpatterns = [
    #swager
    path('swagger/', xframe_options_sameorigin(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("api/",include('api.urls')),
    path('admin/', admin.site.urls),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}), 
]
