from django.db import models
from django.conf import settings


class ExternalProvider(models.Model):
    """Directory of the sleep physicians / ENTs / oral surgeons / dentists /
    OMFTs the practice refers to and from -- shown only inside the
    password-protected portal, per client's 'hidden button, password
    protected area' instruction."""

    name = models.CharField(max_length=200)
    specialty = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.specialty})"


class ReferralSubmission(models.Model):
    """A referral sent by a logged-in external provider, optionally with
    attached patient images/DICOM/notes."""

    class ReferralType(models.TextChoices):
        ORTHO_AIRWAY_CHILD = "ortho_airway_child", "Ortho / Dento-facial / Airway (child)"
        TMJ = "tmj", "TMJ"
        OSA_AIRWAY_ADULT = "osa_airway_adult", "OSA / Airway (adult)"
        MYOFUNCTIONAL = "myofunctional", "Myofunctional therapy"
        OTHER = "other", "Other"

    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="referrals")
    referral_type = models.CharField(max_length=30, choices=ReferralType.choices)
    patient_name = models.CharField(max_length=200)
    patient_dob = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    attachment = models.FileField(upload_to="referrals/attachments/", blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    office_reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"Referral: {self.patient_name} from {self.submitted_by}"
