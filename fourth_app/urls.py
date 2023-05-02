from django.urls import path
from . import views

app_name='fourth_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special'),
]
