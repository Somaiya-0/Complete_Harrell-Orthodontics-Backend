from django.db import models


class VideoTestimonial(models.Model):
    """
    Patient testimonial / educational videos. Supports either a hosted
    `video_url` (YouTube/Vimeo/etc.) or a directly uploaded `video_file` --
    staff can use whichever they have. `page` optionally assigns the video
    to a specific CMS page so the multi-page content-mapping requirement
    is satisfied for videos, not just text/image sections.
    """

    class Category(models.TextChoices):
        PATIENT_TESTIMONIAL = "patient_testimonial", "Patient testimonial"
        EDUCATIONAL = "educational", "Educational"
        OFFICE_TOUR = "office_tour", "Office tour"

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30, choices=Category.choices, default=Category.PATIENT_TESTIMONIAL)
    video_url = models.URLField(blank=True, help_text="YouTube/Vimeo/hosted URL (leave blank if uploading a file instead)")
    video_file = models.FileField(upload_to="videos/uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="videos/thumbnails/", blank=True, null=True)
    caption_text = models.TextField(blank=True, help_text="Subtitle/transcript text shown with the video.")
    page = models.ForeignKey(
        "pages.Page", on_delete=models.SET_NULL, null=True, blank=True, related_name="videos",
        help_text="Optionally assign this video to a specific page.",
    )
    order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
