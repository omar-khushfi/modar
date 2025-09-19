from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services_list, name="services"),
    path("news/", views.news_list, name="news_list"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("projects/", views.projects_list, name="projects"),
    path("contact/", views.contact_view, name="contact"),
    path("about_us/", views.about_us, name="about_us"),
    
]
