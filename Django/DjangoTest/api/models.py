from django.db import models

# models_list = [
#     'AutoField', 'BLANK_CHOICE_DASH', 'BigAutoField', 'BigIntegerField',
#     'BinaryField', 'BooleanField', 'CharField', 'CommaSeparatedIntegerField',
#     'DateField', 'DateTimeField', 'DecimalField', 'DurationField',
#     'EmailField', 'Empty', 'Field', 'FieldDoesNotExist', 'FilePathField',
#     'FloatField', 'GenericIPAddressField', 'IPAddressField', 'IntegerField',
#     'NOT_PROVIDED', 'NullBooleanField', 'PositiveIntegerField',
#     'PositiveSmallIntegerField', 'SlugField', 'SmallIntegerField', 'TextField',
#     'TimeField', 'URLField', 'UUIDField',
# ]

# null 当该字段为空时Django会将数据库中该字段设置为 NULL
# blank 涉及表单验证方面 如果一个字段设置为 blank=True在进行表单验证时接收的数据该字段值允许为空
# default 字段的默认值
# help_text 帮助文档
# unique 字段必须在整个表中保持值唯一
# primary_key 自动设置主键

# class UserInfo(models.Model):
#     # CharField
#     username = models.CharField("person's name", max_length=255, primary_key=True)
#     password = models.CharField(max_length=255)
#     # CharField Choices
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
#     update_tms = models.DateTimeField(auto_now=True)
#     insert_tms = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.username
#
#     # get_absolute_url()
#     # 使用内部 Meta类来给模型赋予元数据
#     class Meta:
#         ordering = ["username"]
#
#
# class ShirtInfo(models.Model):
#     # verbose_name 获取字段名称
#     # ForeignKey
#     poll = models.ForeignKey(
#         UserInfo,
#         on_delete=models.CASCADE,
#         verbose_name="the related poll",
#     )
#     # ManyToManyField
#     sites = models.ManyToManyField(UserInfo, verbose_name="list of sites")
#     # OneToOneField
#     place = models.OneToOneField(
#         UserInfo,
#         on_delete=models.CASCADE,
#         verbose_name="related place",
#     )
#
#     def __str__(self):
#         return self.place

###################################################################################
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    organization = models.CharField('Organization', max_length=200, blank=True)
    telephone = models.CharField('Telephone', max_length=200, blank=True)
    modification_date = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return self.user.__str__()
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################