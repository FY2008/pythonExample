from django.db import models


class BaseModel(models.Model):
    """models.py
    模型基础
    """
    created = models.DateTimeField('创建日期', auto_now_add=True)
    created_date = models.DateTimeField('更新日期', auto_now=True)

    is_deleted = models.BooleanField('是否已删除', default=False)
    is_active = models.BooleanField('是否激活', default=True)

    class Meta:
        abstract = True
        ordering = ['-created']
