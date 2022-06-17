from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True, null=False, editable=False, blank=False, verbose_name='登録日時')
    updated_at = models.DateTimeField(auto_now=True, null=False, editable=False, blank=False, verbose_name='最終更新日時')

    class Meta:
        db_table = 'users'
        verbose_name = verbose_name_plural = 'ユーザー'
