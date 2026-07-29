from django.db import models


class Publication(models.Model):
    class Kind(models.TextChoices):
        ARTICLE = "article", "Journal article"
        BOOK_CHAPTER = "book_chapter", "Book chapter"
        BOOK = "book", "Book"
        PATENT = "patent", "Patent"

    title = models.CharField(max_length=300)
    kind = models.CharField(max_length=20, choices=Kind.choices)
    authors = models.CharField(max_length=300, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-year", "order"]

    def __str__(self):
        return self.title


class Event(models.Model):
    class Kind(models.TextChoices):
        LECTURE = "lecture", "Lecture / Course"
        EVENT = "event", "Event"
        WEBINAR = "webinar", "Webinar"

    title = models.CharField(max_length=300)
    kind = models.CharField(max_length=20, choices=Kind.choices)
    audience = models.CharField(max_length=200, blank=True, help_text="e.g. Doctors, Allied HC professionals, Public")
    starts_at = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    fee = models.CharField(max_length=100, blank=True)
    registration_url = models.URLField(blank=True)

    class Meta:
        ordering = ["starts_at"]

    def __str__(self):
        return self.title
