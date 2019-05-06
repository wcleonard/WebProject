from django.views import generic, View
from django.utils import timezone

from django.shortcuts import (
    render_to_response,
    render,
    redirect,
    reverse,
    resolve_url,
    get_object_or_404,
    get_list_or_404
)

from django.http import (
    HttpResponse,
    JsonResponse,
    QueryDict,
    SimpleCookie,
    parse_cookie,
    HttpResponseRedirect)

from . import models
from . import forms


#################################################################################
# login
# from django.contrib import auth
# # csrf_exempt
# from django.views.decorators.csrf import csrf_exempt
# from django.core.exceptions import ValidationError
#
#
# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         form = forms.LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = auth.authenticate(username=username, password=password)
#             if user is not None and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect('/api/index/')
#             else:
#                 return render(request, 'user/login.html', {'form': form, 'message': 'Wrong login'})
#     else:
#         form = forms.LoginForm()
#     return render(request, 'user/login.html', {'form': form})


#################################################################################
# register

# @csrf_exempt
# def register(request):
#     if request.method == "POST":
#         form = forms.RegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             email = form.cleaned_data['email']
#             # save to User
#             # 会把密码生成哈希值
#             try:
#                 user = models.User.objects.create_user(
#                     username=username,
#                     password=password,
#                     email=email
#                 )
#             except ValidationError as e:
#                 return render(request, 'user/register.html', {'form': form, 'message': 'register error'})
#             user_profile = models.UserProfile(user=user)
#             user_profile.save()
#             return HttpResponseRedirect('/api/login/')
#     else:
#         form = forms.RegisterForm()
#     return render(request, 'user/register.html', {'form': form})


#################################################################################
class IndexView(generic.ListView):
    model = models.Question
    template_name = 'wcp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return models.Question.objects.filter(publish_date__lte=timezone.now())


#################################################################################
# send Email

# from django.core.mail import send_mail
# from .forms import ContactForm
# from django.conf import settings
#
#
# def mail_form(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             receiver = form.cleaned_data['receiver']
#             cc_myself = form.cleaned_data['cc_myself']
#
#             recipients = [receiver]
#             if cc_myself:
#                 recipients.append(settings.EMAIL_HOST_USER)
#
#             sender = settings.EMAIL_HOST_USER
#             send_mail(subject, message, sender, recipients)
#             return HttpResponseRedirect('/api/index/')
#     else:
#         form = ContactForm()
#
#     return render(request, 'user/email.html', {'form': form})

#################################################################################
from django.db.models import Q, F

# Q 主要作用是对对象的复杂查询
# F 主要作用是操作数据表中某列值

#################################################################################
