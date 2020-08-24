from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='media/avatar/', default='/media/avatar/default_male_avatar.png',
                               blank=True, verbose_name='头像')
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), max_length=6, default='male',
                              verbose_name='性别')
    phone = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    status = models.CharField(choices=(('1', '正常'), ('0', '停用')), default='1', max_length=1, verbose_name='状态')

    class Meta:
        verbose_name_plural = verbose_name = '用户信息'

    def __str__(self):
        return self.user.username
