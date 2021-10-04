from django.urls import path

import authapp.views as authapp
from .views import login, logout, register, edit

app_name = 'authapp'
urlpatterns =[
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
]