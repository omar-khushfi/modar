from django.contrib import admin
from .models import Service, Project, News, ContactMessage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured")
    list_filter = ("is_featured",)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("category",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "service", "created_at", "is_handled")
    list_filter = ("service", "is_handled")
    readonly_fields = ("name", "email", "phone", "service", "message", "created_at")
