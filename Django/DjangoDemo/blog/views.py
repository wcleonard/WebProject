from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'blog/index.html')


def blog_list(request):
    return render(request, 'blog/blog-left-sidebar.html')


def blog_detail(request):
    return render(request, 'blog/blog-details.html')


def login(request):
    return render(request, 'blog/github_login.html')


def register(request):
    return render(request, 'blog/register.html')
