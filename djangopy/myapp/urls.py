from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name="home"), 
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register, name="register"),
    path('add_account/', views.add_main_account, name='add_account'),
    path('add_sub_account/', views.add_sub_account, name='add_sub_account'),
    path('add_product/', views.add_product, name='add_product'),
    

]