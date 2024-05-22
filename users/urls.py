from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.dashboardPage, name='dashboard'),
    
    path('register/', views.registerPage, name='register-page'),
    
    path('user-products/<str:pk>', views.userProducts, name='user-products'),
    
    # path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('user/update-profile/', views.updateProfile, name='update-profile'),

]