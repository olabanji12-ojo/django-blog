from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('registerpage/', views.registerpage, name='registerpage'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('delete_message/<int:id>/', views.delete_message, name='delete_message'),
    

]
