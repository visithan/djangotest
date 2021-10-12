from django.urls import path
from . import views

urlpatterns = [
    path('', views.userlogin, name="login"),
    path('register/', views.userregistration, name="register"),
    #path('logout/', views.userlogout),
]