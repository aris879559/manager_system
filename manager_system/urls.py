"""
URL configuration for manager_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from jobs.views import *
from interview.views import *
#定义多语言翻译，_表示多语言
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('joblist/', joblist,name="joblist"),
    path('job/<int:job_id>/', jobdetail,name="jobdetail"),
    path('upload_csv/', upload_csv,name="upload_csv"),
    path('accounts/', include('registration.backends.simple.urls')),
]

admin.site.site_header = _("鑫鑫科技招聘管理系统")


