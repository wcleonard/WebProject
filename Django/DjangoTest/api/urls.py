from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    # login
    path('login/', views.login, name='login'),
    # register
    path('register/', views.register, name='register'),
    # get user info
    path('logout/', views.logout, name='logout'),
    # username
    path('username/', views.form_example, name='username'),
    # email login
    path('email/', views.mail_form, name='email'),
    # login by github
    path('login/', views.github_login, name='login'),
    path('', include('social_django.urls', namespace='social')),
]
