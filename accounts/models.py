from django.db import models
from django.contrib.auth.models import AbstractUser

school_select = (
    ("고려대학교", "고려대학교"),
    ("국민대학교", "국민대학교"),
    ("동덕여자대학교", "동덕여자대학교"),
    ("서경대학교", "서경대학교"),
    ("성신여자대학교", "성신여자대학교"),
    ("한국예술종합학교", "한국예술종합학교"),
    ("한성대학교", "한성대학교"),
)

class MyUser(AbstractUser, models.Model):
    school = models.CharField(max_length=10, choices=school_select, default="고려대학교")
    realname = models.CharField(max_length=20, blank=True, null=True)
    # mycode = models.URLField(blank=True, null=True)
