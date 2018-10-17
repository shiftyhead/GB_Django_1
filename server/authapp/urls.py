from django.urls import path, re_path
import authapp.views as authapp
from .views import LoginView
app_name = 'auth'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', authapp.logout, name='logout'),
    re_path(r'^register/$', authapp.register, name='register'),
    re_path(r'^edit/$', authapp.edit, name='edit'),

]
