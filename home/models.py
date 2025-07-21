# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    username = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Members(models.Model):

    #__Members_FIELDS__
    memberno = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Members_FIELDS__END

    class Meta:
        verbose_name        = _("Members")
        verbose_name_plural = _("Members")


class Contributions(models.Model):

    #__Contributions_FIELDS__
    contributionno = models.IntegerField(null=True, blank=True)
    memberno = models.ForeignKey(members, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)

    #__Contributions_FIELDS__END

    class Meta:
        verbose_name        = _("Contributions")
        verbose_name_plural = _("Contributions")



#__MODELS__END
