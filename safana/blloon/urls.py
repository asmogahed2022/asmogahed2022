from django import views
from django.urls import path
from . import views
from .views import  BlogPageView, ContentPageView, HomePageView, LoginView  # new

urlpatterns = [
    
    path("", HomePageView.as_view(), name="home"),
    path('index/',views.index,name='index'),
    path('show/',views.show,name='show'),
    path("blog/", BlogPageView.as_view(), name="blog"),  # new
    path("content/", ContentPageView.as_view(), name="content"),
    path("offers/",views.offers, name="offers"),
    path('index/create',views.create,name="create"), # new
    path('login/', LoginView.as_view(), name='login'),
    path('signup/pages/login/', LoginView.as_view(), name='login'),
    path('signup/', views.signup, name="signup"),
    path('delete/<int:id>', views.destroy), 
    path('edit/<int:id>', views.edit),   
    path('update/<int:id>', views.update),  
    path('ForgetPassword', views.ForgetPassword,name='ForgetPassword'),
    path('signup/pages/login/login', views.ForgetPassword,name='ForgetPassword'),
    


]
