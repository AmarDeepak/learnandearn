from home import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view({'get':'get'}), name='Home'),
]