from django.db import models


class FinancingOption(models.Model):
    """
    Ordered list of financing options. Client instruction (email 6/29 and
    7/9): Cherry must be the PRIMARY option -- shown first, made to stand
    out, above Credit Cards / CareCredit. `order` (ascending) controls
    display order, `is_primary` drives the larger/highlighted widget
    styling on the frontend.
    """

    class Kind(models.TextChoices):
        CHERRY = "cherry", "Cherry"
        CREDIT_CARDS = "credit_cards", "Credit Cards"
        HSA = "hsa", "Health Savings Accounts (HSA)"
        HEALTH_FINANCING_DIRECT = "health_financing_direct", "Health Financing Direct"
        CARECREDIT = "carecredit", "CareCredit"

    kind = models.CharField(max_length=40, choices=Kind.choices, unique=True)
    display_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="financing/", blank=True, null=True)
    tagline = models.CharField(max_length=200, blank=True)
    learn_more_url = models.URLField(blank=True)
    widget_script_url = models.URLField(
        blank=True, help_text="Cherry Widget Builder output URL (full-page + floating button)."
    )
    is_primary = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.display_name
