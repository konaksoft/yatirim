import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    job_title = models.CharField(max_length=120, blank=True, null=True)
    mobile_phone = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(upload_to='accounts/', null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['first_name']



