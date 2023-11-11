from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    email = models.EmailField(unique=True)
    institution = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    # 可能还需要一些额外的字段，比如用户角色的标识符等
    # 用related_name解决冲突
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_set",
        blank=True,
        help_text='Specific permissions for this user.'
    )
