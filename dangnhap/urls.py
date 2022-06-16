from django.urls import path
from .import views

app_name = 'dangnhap'
urlpatterns = [
    path('',views.signupUser.as_view(),name='signupUser'),
]
# python manage.py runserver localhost:18080