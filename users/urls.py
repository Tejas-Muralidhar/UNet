from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('update/', views.update_user, name='update_user'),
    path('create/', views.create_user, name='create_user'),
    path('profile/', views.view_user, name='view_user'),
]
