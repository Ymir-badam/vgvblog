from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    """A firm update / insight article, manageable from the Django admin."""

    CATEGORY_CHOICES = [
        ("taxation", "Taxation"),
        ("gst", "GST"),
        ("compliance", "Corporate Compliance"),
        ("accounting", "Accounting & Bookkeeping"),
        ("audit", "Internal Audit & Risk"),
        ("payroll", "Payroll & Statutory"),
        ("general", "General / Firm News"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="general")
    excerpt = models.CharField(
        max_length=300,
        blank=True,
        help_text="Short summary shown on the homepage and post list. Auto-filled from content if left blank.",
    )
    content = models.TextField(help_text="Main body of the post. Plain paragraphs, one per line, are fine.")
    cover_image = models.ImageField(upload_to="posts/%Y/%m/", blank=True, null=True)
    author = models.CharField(max_length=120, default="VGV Konsultancy")
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        if not self.excerpt:
            stripped = self.content.strip()
            self.excerpt = (stripped[:280] + "…") if len(stripped) > 280 else stripped
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("website:post_detail", kwargs={"slug": self.slug})

    @property
    def paragraphs(self):
        """Split content into paragraphs for simple template rendering."""
        return [p.strip() for p in self.content.split("\n") if p.strip()]
