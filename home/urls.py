from django.urls import path

from .views import *

# from home import views

urlpatterns = [
    path("", index, name='home'),
    path("about", about, name='about'),
    path("services", services, name='services'),
    path("products", products, name='product'),
    path("contact", contact, name='contact'),
    path("signup", signupUser, name='signup'),
    path("login", loginUser, name='login'),
    path("logout", logoutUser, name='logout'),

]
