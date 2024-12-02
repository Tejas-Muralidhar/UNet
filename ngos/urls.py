from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_ngo, name='login_ngo'),
    path('logout/', views.logout_ngo, name='logout_ngo'),
    path('update/', views.update_ngo, name='update_ngo'),
    path('create/', views.create_ngo, name='create_ngo'),
    path('profile/', views.view_ngo, name='view_ngo'),
]
