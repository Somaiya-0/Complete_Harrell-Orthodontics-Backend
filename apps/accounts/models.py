from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user. 'staff' manage content via Django Admin (is_staff).
    'referrer' accounts are external doctors/providers who log into the
    password-protected referral portal to send patient notes/images.
    """

    class Role(models.TextChoices):
        STAFF = "staff", "Practice Staff"
        REFERRER = "referrer", "Referring Provider"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.REFERRER)
    practice_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.role})"
