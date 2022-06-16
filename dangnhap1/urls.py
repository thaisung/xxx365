from django.urls import path
from .import views

app_name = 'dangnhap1'
urlpatterns = [
    path('',views.dangnhap1 ),
    path('getFile/',views.getFile,name='getFile'),
]
# python manage.py runserver localhost:18080