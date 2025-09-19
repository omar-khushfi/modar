from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["title"]
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["title"]
        verbose_name = "مشروع"
        verbose_name_plural = "المشاريع"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.CharField(max_length=100, blank=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "الأخبار"

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ("structural", "تصميم إنشائي"),
        ("consulting", "استشارات هندسية"),
        ("testing", "فحوصات مختبرية"),
        ("supervision", "إشراف هندسي"),
        ("other", "خدمات أخرى"),
    ]
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "رسالة"
        verbose_name_plural = "رسائل التواصل"

    def __str__(self):
        return f"{self.name} - {self.service}"
