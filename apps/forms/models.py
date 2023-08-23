import uuid
from django.db import models



class Forms(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    step1 = models.TextField(null=True, blank=True)
    step2 = models.TextField(null=True, blank=True)
    step3 = models.TextField(null=True, blank=True)
    step4 = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    GENDER_CHOICES = ((0, 'Erkek'), (1, 'Kadın'))
    gender = models.IntegerField(choices=GENDER_CHOICES)

    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField()


    class Meta:
        db_table = 'Forms'
