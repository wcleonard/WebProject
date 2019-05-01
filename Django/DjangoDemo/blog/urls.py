from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_list, name='blog_list'),
    path('details/', views.blog_detail, name='blog_detail'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]