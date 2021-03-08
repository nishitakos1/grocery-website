from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("products/<int:myid>", views.productview, name="ProductView"),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='Search'),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path('checkout/', views.Checkout, name='Checkout'),
    path('tracker/', views.Tracker, name='Tracker'),

]
