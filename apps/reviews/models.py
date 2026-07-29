from django.db import models


class Review(models.Model):
    class Source(models.TextChoices):
        GOOGLE = "google", "Google"
        FACEBOOK = "facebook", "Facebook"
        WEBSITE = "website", "Submitted on website"
        OTHER = "other", "Other"

    author_name = models.CharField(max_length=150)
    source = models.CharField(max_length=20, choices=Source.choices, default=Source.WEBSITE)
    rating = models.PositiveSmallIntegerField(default=5)
    body = models.TextField()
    review_date = models.DateField(null=True, blank=True, auto_now_add=False)
    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False, help_text="Reviews submitted on the site require staff approval before they show publicly.")
    submitted_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-review_date"]

    def __str__(self):
        status = "✓" if self.is_approved else "(pending)"
        return f"{self.author_name} ({self.rating}★, {self.source}) {status}"