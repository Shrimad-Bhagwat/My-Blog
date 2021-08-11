from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path('coding', views.coding, name="coding"),
    path('nature', views.nature, name="nature"),
    path('travel', views.travel, name="travel"),
    path('feedback', views.feedback, name="feedback"),
    path('create', views.create, name="create"),
]
