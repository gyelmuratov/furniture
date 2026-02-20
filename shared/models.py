from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to="home/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class HomeSlider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="home/slider/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="about/", blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    map_link = models.URLField(blank=True)

    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    title = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
