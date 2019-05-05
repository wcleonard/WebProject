from django.db import models

from django.utils import timezone


##################################################################################
class Question(models.Model):
    question_text = models.CharField(max_length=60)
    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return self.publish_date <= now


##################################################################################

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


##################################################################################

# models list

# AutoField             =>  根据ID自动递增(如果没有指定则主键字段会自动添加)
# BigAutoField          =>  字段是64位整数(取值范围是从1 ~ 9223372036854775807)
# BigIntegerField       =>  字段是64位整数(-9223372036854775808 ~ 9223372036854775807)
# BinaryField           =>  存储二进制数据字段(bytes、bytearray、memoryview)
# BooleanField          =>  字段是存储真/假(默认表单窗口小部件是CheckboxInput)
# CharField             =>  字符串字段用于小到大的字符串
# DateField             =>  date(默认表单窗口小部件是a TextInput)
# DateTimeField         =>  datetime
# DecimalField          =>  一个固定精度的十进制数(两个必需的参数: max_digits(数字中允许的最大位数) 和 decimal_places(与数字一起存储的小数位数))
# DurationField         =>  存储时间段的字段(用Python建模 timedelta)
# EmailField            =>  存储有效的电子邮件地址(EmailValidator)
# FileField             =>  文件上传字段(参数：upload_to)
# FilePathField         =>  选择仅限于文件系统上某个目录中的文件名(path match recursive)
# FloatField            =>  由float实例在Python中表示的浮点数
# ImageField            =>  上载的对象是有效图像
# IntegerField          =>  整数(-2147483648 ~ 2147483647)
# GenericIPAddressField =>  IPv4或IPv6地址(例如192.0.2.30或 2a02:42fe::4)
# PositiveIntegerField  =>  必须是正面或零(0 ~ 2147483647的所有数据)
# PositiveSmallIntegerField => (0 ~ 32767的所有数据)
# SlugField             =>  短标签(只包含字母、数字、下划线或连字符通常用于URL)
# SmallIntegerField     =>  (-32768 ~ 32767的所有数据)
# TextField             =>  文本字段
# TimeField             =>  由datetime.time实例表示(相同的自动填充DateField)
# URLField              =>  URL(经过验证 URLValidator)
# UUIDField             =>  存储唯一标识符的字段(使用Python的 UUID 类)

##################################################################################

# field options

# null                  =>  当该字段为空时会将数据库中该字段设置为 NULL
# blank                 =>  涉及表单验证方面 在进行表单验证时接收数据该字段值允许为空
# default               =>  设置字段的默认值
# help_text             =>  帮助文档
# unique                =>  字段必须在整个表中保持值唯一
# primary_key           =>  给字段自动设置主键
# choices               =>  默认该字段是一个选择框
# db_index              =>  如果True，将为此字段创建数据库索引
# db_tablespace         =>  如果此字段已编制索引，则用于此字段索引的数据库表空间的名称
# db_column             =>  用于此字段的数据库列的名称
# editable              =>  如果设置False该字段将不会显示在管理员或任何其他字段中 ModelForm
# error_messages        =>  该参数允许您覆盖该字段将引发的默认消息
# unique_for_date
# unique_for_month
# unique_for_year
# verbose_name          =>  该字段的可读名称如果未给出详细名称将使用字段的属性名称自动创建它并且将下划线转换为空格
# validators            =>  要为此字段运行的验证程序列表

##################################################################################
# person model

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    # CharField Choices
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField()


##################################################################################
# 关系

# ForeignKey            =>  多对一关系
# OneToOneField         =>  一对一关系
# ManyToManyField       =>  多对多关系

##################################################################################
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


##################################################################################
# Meta options --- 使用内部提供模型元数据

# 可用Meta元选项
# abstract              =>  abstract = True 则这个模型将是一个抽象基类
# app_label             =>  在应用程序之外定义模型
# base_manager_name     =>  用于模型的管理器的名称
# db_table              =>  数据库表名
# db_tablespace         =>  用于此模型的数据库表空间的名称
# default_manager_name  =>  用于模型的管理器的名称
# default_related_name  =>  默认情况下将用于从相关对象返回到此对象的关系的名称
# get_latest_by         =>  字段的名称或字段名称的模型的列表
# managed               =>  默认为True，意味着Django将在migrate迁移中或作为迁移的一部分创建适当的数据库表
# order_with_respect_to =>  使该对象相对于给定字段可订购
# ordering              =>  排序字段
# permissions           =>  创建此对象时进入权限表的额外权限(为每个模型自动创建添加、更改、删除和查看权限)
# default_permissions   =>  您可以自定义此列表，例如，如果您的应用不需要任何默认权限，则将其设置为空列表
# proxy                 =>  将另一个模型子类化的模型视为代理模型
# required_db_features  =>  当前连接应具有的数据库功能列表，以便在迁移阶段考虑模型
# required_db_vendor    =>  支持数据库供应商的名称(内置供应商名称有：sqlite、postgresql、mysql、oracle)
# select_on_save        =>  选择保存
# indexes               =>  要在模型上定义的索引列表
# unique_together       =>  列表(这些列表在一起考虑时必须是唯一的)
# index_together        =>  这个字段列表将被索引在一起
# constraints           =>  要在模型上定义的约束列表
# verbose_name          =>  可读的单数名称
# verbose_name_plural   =>  可读的复数名称

# 只读Meta属性(Options.label、Options.label_lower)

##################################################################################
# 模型方法 --- 在模型上定义自定义方法以向对象添加自定义“行级”功能

# __str__()          返回任何对象的字符串表示形式
# get_absolute_url() 这告诉Django如何计算对象的URL

##################################################################################
# 覆盖预定义的模型方法 --- 封装了一些您想要自定义的数据库行为
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagLine = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return  # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.


##################################################################################

##################################################################################
# 模型继承
##################################################################################
# Django有三种可能的继承方式
#   (1)通常只想使用父类来保存您不希望为每个子模型键入的信息(这个类不会被孤立使用所以抽象基类就是你所追求的)
#   (2)如果你是现有模型的子类（可能是完全来自另一个应用程序的东西）并希望每个模型都有自己的数据库表(多表继承是最佳选择)
#   (3)如果您只想修改模型的Python级行为而不以任何方式更改模型字段则可以使用代理模型
##################################################################################

##################################################################################
# (1) 抽象基类
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    # Meta继承
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'


# 注意
# related_name和related_query_name
# 则必须始终为该字段指定唯一的反向名称和查询名称
# 这通常会导致抽象基类出现问题
# 因为此类中的字段包含在每个子类中每次都具有完全相同的属性值

##################################################################################

##################################################################################
# (2)多表继承
# 当层次结构中的每个模型都是模型本身时
# 每个模型对应于自己的数据库表可以单独查询和创建
# 继承关系引入子模型与其每个父模型之间的链接
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)


# Meta和多表继承
#   在多表继承情况下子类从其父类的Meta类继承是没有意义的

# 继承和反向关系
#   由于多表继承使用隐式 OneToOneField链接子项和父项，因此可以从父项向下移动到子项
#   如果要将这些类型的关系放在父模型的子类上，则 必须 在每个此类字段上指定该属性

# 指定父链接字段
#   创建自己的属性OneToOneField并设置 parent_link=True 为指示您的字段是返回父类的链接
##################################################################################
# 代理模型 --- 为原始模型创建代理
# 可能更改默认管理器或添加新方法

class PersonView(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    class Meta:
        # 通过设置类的proxy属性告诉Django它是一个代理模型
        proxy = True

    def do_something(self):
        pass


##################################################################################
# (3)多重继承 --- Django模型可以从多个父模型继承
# 向每个继承混合的类添加特定的额外字段或方法尽量使您的继承层次结构尽可能简单明了
class Piece(models.Model):
    pass


class Article(Piece):
    article_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)


class Book(Piece):
    book_piece = models.OneToOneField(Piece, on_delete=models.CASCADE, parent_link=True)


class BookReview(Book, Article):
    pass

##################################################################################
# 模型索引参考 --- Index选项

# classIndex(fields=(), name=None, db_tablespace=None, opclasses=(), condition=None)

# Index.fields      =>      要求索引的字段名称的列表或元组

# Index.name        =>      索引的名称

# Index.tablespace  =>      用于此索引的数据库表空间的名称

# Index.opclasses   =>      用于此索引的PostgreSQL运算符类的名称。如果需要自定义运算符类，则必须为索引中的每个字段提供一个

# Index.condition   =>      如果表非常大并且您的查询主要针对行的子集，则将索引限制为该子集可能很有​​用
# 将条件指定为 Q 例如 condition=Q(pages__gt=400) 索引记录超过400页

##################################################################################
# QuerySets
##################################################################################
# (1) Making queries

# 模型类表示数据库表，该类的实例表示数据库表中的特定记录

# from blog.models import Blog
# b = Blog(name='Beatles Blog', tag='All the latest Beatles news.')
# b.save()

# 保存对象的更改
# b.name = 'New name'
# b.save()

# 保存ForeignKey和ManyToManyField字段
# from blog.models import Blog, Entry
# entry = Entry.objects.get(pk=1)
# cheese_blog = Blog.objects.get(name='Cheddar Talk')
# entry.blog = cheese_blog
# entry.save()
# 更新ManyToManyField工作的方式略有不同
# >>> from blog.models import Author
# >>> joe = Author.objects.create(name="Joe")
# >>> entry.authors.add(joe)
# 检索对象 Blog.objects

# 检索所有对象
# >>> all_entries = Entry.objects.all()

# 使用过滤器检索特定对象
# Entry.objects.all().filter(pub_date__year=2006)

# >>> q1 = Entry.objects.filter(headline__startswith="What")
# >>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
# >>> q3 = q1.filter(pub_date__gte=datetime.date.today())

# QuerySets是很懒的

# >>> Entry.objects.all()[5:10]

# >>> Entry.objects.filter(blog_id=4)
##################################################################################
# exact --- “精确”匹配
# >>> Entry.objects.get(headline__exact="Cat bites dog")

# iexact --- 不区分大小写的匹配项
# >>> Blog.objects.get(name__iexact="beatles blog")

# contains --- 区分大小写的遏制测试
# Entry.objects.get(headline__contains='Lennon')

# startswith， endswith --- 分别以搜索开始和结束

# Django提供了一个pk查找快捷方式，代表“主键”

# 过滤器可以引用模型上的字段
# from django.db.models import F

# 使用Q对象进行复杂查找
# from django.db.models import Q
# Q(question__startswith='What')

# 删除对象 e.delete()

##################################################################################

# (2) QuerySet method reference

##################################################################################

# (3) Lookup expressions

##################################################################################

##################################################################################
