"""CollegeManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from college.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('about',About,name="about"),
    path('nav',nav,name="nav"),
    path('login',Login,name="login"),
    path('signup',SignUp,name="signup"),
    path('loginadmin',Admin_Login,name="loginadmin"),
    path('adminhome',Admin_home,name="adminhome"),
    path('userhome',User_home,name="userhome"),
    path('userdetail',Userdetail,name="userdetail"),
    path('coursedetail',Course_detail,name="coursedetail"),
    path('noticedetail',Notice_detail,name="noticedetail"),
    path('logout',Logout,name="logout"),
    path('addcourse',Add_Course,name="addcourse"),
    path('addnotice',Add_Notice,name="addnotice"),
    path('contact',Contact,name="contact"),
    path('view_notice(?P<int:pid>)',View_Notice,name="view_notice"),
    path('admission',Admission_form,name="admission"),
    path('viewdetail(?P<pid>[0-9]+)',View_detail,name="viewdetail"),
    path('upload_doc',Upload_doc,name="upload_doc"),
    path('view_doc(?P<pid>[0-9]+)',view_doc,name="view_doc"),
    path('delete_user(?P<pid>[0-9]+)',delete_user,name="delete_user"),
    path('delete_course(?P<pid>[0-9]+)',delete_course,name="delete_course"),
    path('delete_notice(?P<pid>[0-9]+)',delete_notice,name="delete_notice"),
    path('change_password',Change_Password,name="change_password"),
    path('view_application(?P<str:status>)',View_Applicant,name="view_application"),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
