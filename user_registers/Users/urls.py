from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegisterUser, name='register'),
    path('success/', views.Sucess, name='success'),
    path('users/', views.ListRegisters, name='list_registers'),
    path('users/delete/<int:user_id>/', views.DeleteUser, name='delete_user'),
    path('users/update/<int:user_id>/', views.UpdateUser, name='update_user'),
]