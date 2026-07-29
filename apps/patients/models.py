from django.db import models


class PatientFormSubmission(models.Model):
    """
    Online 'New Patient' intake form submission.
    """

    class ReasonForVisit(models.TextChoices):
        ORTHODONTIC = "orthodontic", "Orthodontic / Braces evaluation"
        TMJ = "tmj", "TMJ / Jaw pain"
        SLEEP_AIRWAY = "sleep_airway", "Sleep / Airway / Snoring"
        SECOND_OPINION = "second_opinion", "Second opinion"
        OTHER = "other", "Other"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    email = models.EmailField()
    phone = models.CharField(max_length=30)

    reason_for_visit = models.CharField(
        max_length=30,
        choices=ReasonForVisit.choices
    )

    is_new_patient = models.BooleanField(default=True)

    referred_by = models.CharField(
        max_length=200,
        blank=True
    )

    has_sleep_study = models.BooleanField(default=False)

    sleep_study_file = models.FileField(
        upload_to="patient_uploads/sleep_studies/",
        blank=True,
        null=True
    )

    notes = models.TextField(blank=True)

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    office_reviewed = models.BooleanField(
        default=False
    )


    class Meta:
        ordering = ["-submitted_at"]


    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} "
            f"— {self.get_reason_for_visit_display()}"
        )





class Patient(models.Model):
    """
    Actual patient-of-record managed by staff dashboard.
    This is different from PatientFormSubmission, which is only
    an online intake submission.
    """


    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        COMPLETED = "completed", "Treatment completed"



    class Service(models.TextChoices):

        EARLY_ORTHO = (
            "early_ortho_4_6",
            "Early Orthodontics, Ages 4-6"
        )

        ORTHO_7_11 = (
            "ortho_7_11",
            "Orthodontics, Ages 7-11"
        )

        TEEN_ORTHO = (
            "teen_ortho",
            "Teen Orthodontics"
        )

        ADULT_ORTHO = (
            "adult_ortho",
            "Adult Orthodontics"
        )

        TMJ = (
            "tmj",
            "TMJ Disorders"
        )

        SLEEP_AIRWAY = (
            "sleep_airway",
            "Sleep, Breathing & Airway Disorders"
        )

        MYOFUNCTIONAL = (
            "myofunctional",
            "Myofunctional Therapy"
        )

        AIRWAY_DIAGNOSTICS = (
            "airway_diagnostics",
            "Airway Diagnostics"
        )



    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )


    date_of_birth = models.DateField(
        null=True,
        blank=True
    )


    email = models.EmailField(
        blank=True
    )


    phone = models.CharField(
        max_length=30,
        blank=True
    )


    service = models.CharField(
        max_length=50,
        choices=Service.choices,
        null=True,
        blank=True
    )


    assigned_doctor = models.ForeignKey(
        "team.TeamMember",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="patients"
    )


    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )


    notes = models.TextField(
        blank=True
    )


    source_submission = models.ForeignKey(
        PatientFormSubmission,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="patient_record"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )



    class Meta:
        ordering = [
            "-created_at"
        ]



    def __str__(self):
        return f"{self.first_name} {self.last_name}"






class PatientGallery(models.Model):
    """
    Before and after treatment cases shown on the public
    Patient Gallery page.

    Uploaded and managed only by office staff.
    Not directly connected to patient records.
    """


    title = models.CharField(
        max_length=200
    )


    description = models.TextField(
        blank=True
    )


    treatment = models.CharField(
        max_length=200,
        blank=True
    )


    before_image = models.ImageField(
        upload_to="patient_gallery/before/"
    )


    after_image = models.ImageField(
        upload_to="patient_gallery/after/"
    )


    patient_age = models.CharField(
        max_length=50,
        blank=True
    )


    is_published = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = [
            "-created_at"
        ]


    def __str__(self):
        return self.title