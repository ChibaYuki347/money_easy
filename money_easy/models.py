from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Create your models here.


class PayFor(models.Model):
    """支払い先モデル"""

    class Meta(object):
        # テーブル名を定義
        db_table = 'PayFor'

    # テーブルのカラムに対応するフィールドを定義
    name = models.CharField(verbose_name='人物/組織名', max_length=255)
    description = models.TextField(verbose_name='概要', null=True, blank=True)

    def __str__(self):
        return self.name


class PayItem(models.Model):
    """支払い項目のモデル"""

    class Meta(object):
        db_table = 'PayItem'

    PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))

    title = models.CharField(verbose_name='タイトル',max_length=30,default='title')
    payfor = models.ForeignKey(PayFor, verbose_name='支払先', on_delete=models.PROTECT)
    money = models.IntegerField(verbose_name='金額', null=True, blank=True)
    rate = models.FloatField(verbose_name='利率（年）', default=0.0)
    priority = models.CharField(
        verbose_name='優先度',
        max_length=50,
        choices=PRIORITY,
    )
    duedate = models.DateField(verbose_name='期日', null=True, blank=True)
    memo = models.TextField(verbose_name='備考', null=True,blank=True)

    def __str__(self):
        return self.title


# class CustomUserManager(BaseUserManager):
#     """Define a model manager for USer model with no username field"""
#
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         """Create and save a User with the given email and password"""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user
#
#     def create_user(self,email, password=None, **extra_fields):
#         """Create and save a regular User with the given email and password"""
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('is_superuser must have is_staff=True.')
#
#         return self._create_user(email, password, **extra_fields)
#
#
# class CustomUser(AbstractUser):
#     """拡張ユーザーモデル"""
#
#
#     class Meta(AbstractUser.Meta):
#         db_table = 'custom_user'
#
#         #usernameをオーバーライドして、NULL制約、ユニーク制約、入力必須制限を除去
#         username = models.CharField(
#             'ユーザー名',
#             max_length=150,
#             blank=True,
#             null=True,
#             help_text="半角アルファベット、半角数字、@/./+/-/_で150文字制限にしてください",
#             validators=[AbstractUser.username_validator]
#         )
#
#         #emailをオーバーライドして入力必須制限、ユニーク制限を付与
#         email = models.EmailField('メールアドレス',unique=True)
#
#         USERNAME_FIELD = 'email'
#         REQUIRED_FIELDS = []
#
#         objects = CustomUserManager()