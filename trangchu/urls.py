from django.urls import path
from .import views

app_name = 'trangchu'
urlpatterns = [
    path('',views.uploadFile),
    path('phim/',views.phim,name='phim'),
]
# python manage.py runserver localhost:18080