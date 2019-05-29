from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RiskType(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True
    )
    attribute_collection = JSONField()


class Risk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField("Date Created", auto_now_add=True)
    risk_type = models.ForeignKey(
        RiskType, on_delete=models.SET_NULL,
        null=True
    )





