from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role_title = models.CharField(max_length=150, blank=True)
    credentials = models.CharField(max_length=100, blank=True, help_text="e.g. DMD, C.DSM")
    specialty = models.CharField(max_length=200, blank=True, help_text="e.g. Orthodontist, TMJ & Sleep Medicine")
    bio = models.TextField(blank=True)
    education = models.TextField(blank=True, help_text="One item per line")
    years_experience = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to="team/", blank=True, null=True)
    is_doctor = models.BooleanField(default=False)
    accepting_new_patients = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
