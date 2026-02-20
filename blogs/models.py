from django.db import models


class BlogCategory(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blogs"
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="blogs/")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title