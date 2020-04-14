from django.urls import path
from . import views

urlpatterns = [
    path('holy/', views.holy),
    path('main2/', views.main2, name="main2"),
]
