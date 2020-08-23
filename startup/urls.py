from django.urls import path
from . import views


urlpatterns = [
    path('',views.startups, name='startups' ),
    path('addstartup', views.addstartup, name='addstartup'),
    path('<int:startup_id>/', views.detail, name='detail'),
]
