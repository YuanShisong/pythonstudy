"""demo2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from page import p1  # 将页面引入
from app1 import views

# 注册项目url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', p1.index),  # 前端访问指向后台方法
    # path('app1/view1', views.view1)  # 前端访问指向后台方法
    path('login', views.login),
    path('home', views.home),
]
'''
APPEND_SLASH配置
    APPEND_SLASH=False
        action="login" & path('login', views.login)
            http://127.0.0.1:8000/login 能访问到， http://127.0.0.1:8000/login/ 访问不到
            能跳转
        action="login/" & path('login', views.login)
            http://127.0.0.1:8000/login 能访问到， http://127.0.0.1:8000/login/ 访问不到
            不能跳转
        action="login" & path('login/', views.login)
            http://127.0.0.1:8000/login 访问不到， http://127.0.0.1:8000/login/ 能访问
            不能跳转
        action="login/" & path('login/', views.login)
            需要用http://127.0.0.1:8000/login/ 才能访问到页面, http://127.0.0.1:8000/login 访问不到。
            不能跳转
    APPEND_SLASH=True
        action="login" & path('login', views.login)
            能跳转
        action="login/" & path('login', views.login)
            不能跳转
        action="login" & path('login/', views.login)
            能跳转
        action="login/" & path('login/', views.login)
            不能跳转
'''