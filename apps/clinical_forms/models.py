from django.db import models


class ClinicalFormSubmission(models.Model):
    """
    Digitized versions of the practice's real offline forms (verified
    against the scanned originals in frontend/public/forms-reference/):
    Epworth Sleepiness Scale, STOP-BANG Questionnaire, TMJ Pain Scale,
    C-GASP Screener, CPAP Intolerance Affidavit, and the generic
    referral form. `answers` holds the structured question/answer data
    for whichever form_type this is -- kept as JSON since each form has
    a different real shape rather than forcing one shared schema.
    """

    class FormType(models.TextChoices):
        EPWORTH = "epworth", "Epworth Sleepiness Scale"
        STOP_BANG = "stop_bang", "STOP-BANG Questionnaire"
        TMJ_PAIN_SCALE = "tmj_pain_scale", "TMJ Pain Scale"
        CGASP = "cgasp", "C-GASP Screener"
        CPAP_INTOLERANCE = "cpap_intolerance", "CPAP Intolerance Affidavit"
        REFERRAL = "referral", "Referral Form"

    form_type = models.CharField(max_length=30, choices=FormType.choices)
    patient_name = models.CharField(max_length=200, blank=True)
    submitted_by_name = models.CharField(max_length=200, blank=True, help_text="Referring doctor, if this is a referral")
    answers = models.JSONField(default=dict)
    computed_score = models.CharField(max_length=100, blank=True, help_text="e.g. 'Epworth: 14/24' or 'STOP-BANG: 5 (High Risk)'")
    submitted_at = models.DateTimeField(auto_now_add=True)
    office_reviewed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.get_form_type_display()} \u2014 {self.patient_name or 'unnamed'}"
