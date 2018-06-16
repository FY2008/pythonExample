from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField('昵称', max_length=50, blank=True)
    qq = models.CharField('QQ', max_length=40, blank=True)
    mobile = models.CharField('手机号', max_length=15, blank=True)
    web_site = models.URLField('个人网站', default="http://www.z10.xin")
    avatar = models.ImageField(
        '用户头像',
        upload_to='avatar_folder',
        default='avatar_folder/default.jpg',
        blank=True,
        null=True
        )

    class Meta(AbstractUser.Meta):
        pass
