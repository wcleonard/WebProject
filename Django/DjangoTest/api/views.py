# views 视图的使用
from django.views import View

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
# user login
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/api/index/')
            else:
                return render(request, 'user/login.html', {'form': form, 'message': 'Wrong login'})
    else:
        form = forms.LoginForm()
    return render(request, 'user/login.html', {'form': form})

#################################################################################
# user register
def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            # save to User
            user = models.User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user_profile = models.UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect('/api/login/')
    else:
        form = forms.RegisterForm()
    return render(request, 'user/register.html', {'form': form})

#################################################################################
# logout
def logout(request):
    pass
#################################################################################
#################################################################################
#################################################################################
# 使用CBV模式

class IndexView(View):

    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def get(self, request):
        # dict
        dicts = {
            'message': 'success',
            'code': 200,
            'data': {
                'username': 'admin',
                'password': '147258',
                'datetime': '2019.03.12 12:23:23'
            }
        }
        # string => HttpResponse
        return JsonResponse(dicts)

    def post(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass

    def patch(self, *args, **kwargs):
        pass


#################################################################################
# form example

from .forms import NameForm


def form_example(request):
    # POST request
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # 使用表单提交数据通过调用 is_valid() 验证成功返回 True
            # 已验证的表单数据将被放到 form.cleaned_data 字典中
            print(form.cleaned_data)
            return HttpResponseRedirect('/api/index/')

    # GET request
    else:
        form = NameForm()

    return render(request, 'user/register.html', {'form': form})


#################################################################################
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings


def mail_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            receiver = form.cleaned_data['receiver']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = [receiver]
            if cc_myself:
                recipients.append(settings.EMAIL_HOST_USER)

            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/api/index/')
    else:
        form = ContactForm()

    return render(request, 'user/email.html', {'form': form})


#################################################################################
# github login

def github_login(request):
    return render(request, 'user/github_login.html', locals())

#################################################################################
