# 表单介绍：

# 1.表单作用：构建表单来接收网站访客的输入然后处理以及响应这些输入

# 2.处理表单时只会用到 GET 和 POST 两种HTTP方法
#   登录表单使用 POST 方法传输数据，在这个方法中浏览器会封装表单数据
#   为了传输会进行编码，然后发送到服务端并接收它的响应
#   GET 方法将提交的数据捆绑到一个字符串中并用它来组成一个URL

# 3.Django会处理涉及表单的三个不同部分
#   准备并重组数据，以便下一步的渲染
#   为数据创建HTML 表单
#   接收并处理客户端提交的表单及数据

# 4.forms.Form 类描述一张表单并决定它如何工作及呈现

# 5.当我们实例化表单时，我们可以选择让它为空或者对它预先填充
#   例如使用：
#       来自已保存的模型实例的数据（例如在管理编辑表单的情况下）
#       我们从其他来源获取的数据
#       从前面一个HTML 表单提交过来的数据

#################################################################################

from django import forms

from . import models

#################################################################################
# example
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


#################################################################################

# 每个表单字段都有一个相对应的控件类
# 这个控件类又有对应的HTML表单控件，比如 <input type="text">
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    receiver = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

#################################################################################
# register

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email',)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

#################################################################################
# login

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

#################################################################################

#################################################################################

#################################################################################

#################################################################################
