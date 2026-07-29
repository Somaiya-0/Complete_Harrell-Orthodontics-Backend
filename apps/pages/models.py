from django.db import models


class NavCategory(models.Model):
    """Top-level mega-menu grouping, e.g. 'Orthodontics', 'Airway & Sleep', 'TMJ'."""

    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Nav categories"

    def __str__(self):
        return self.label


class Page(models.Model):
    """
    One flexible content page. Covers every content vertical from the site
    map: Home, Airway tech, Myofunctional therapy, Ortho by age group,
    TMJ Disorders, Sleep/Airway, Patient Gallery, Publications, etc.
    Staff edit these (and their Sections below) in Django Admin -- no code
    change needed to add/update a page.
    """

    nav_category = models.ForeignKey(
        NavCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="pages"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=300, blank=True, help_text="Used in nav tooltips / SEO description")
    hero_image = models.ImageField(upload_to="pages/hero/", blank=True, null=True)
    show_in_nav = models.BooleanField(default=True)
    nav_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nav_category__order", "nav_order", "title"]

    def __str__(self):
        return self.title


class PageSection(models.Model):
    """One content block on a Page. `kind` decides how the frontend renders it."""

    class Kind(models.TextChoices):
        RICH_TEXT = "rich_text", "Rich text"
        IMAGE = "image", "Image with caption"
        VIDEO_EMBED = "video_embed", "Embedded video"
        FORM_LINKS = "form_links", "Downloadable forms list"
        STAT_CALLOUT = "stat_callout", "Highlighted stat / quote"
        CTA = "cta", "Call to action"

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="sections")
    kind = models.CharField(max_length=20, choices=Kind.choices, default=Kind.RICH_TEXT)
    heading = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="pages/sections/", blank=True, null=True)
    video_url = models.URLField(blank=True)
    cta_label = models.CharField(max_length=100, blank=True)
    cta_url = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.page.title} — {self.heading or self.kind}"


class DownloadableForm(models.Model):
    """Patient forms referenced across pages (DW Ortho, C-GASP, PSQ, consent
    forms, etc.) — kept as data so office staff can add/replace PDFs."""

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="forms", null=True, blank=True)
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to="forms/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name
