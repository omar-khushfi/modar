from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, News, Project
from .forms import ContactForm


def home(request):
    services = Service.objects.filter(is_featured=True)[:6]
    return render(
        request,
        "core/home.html",
        {
            "services": services,
           
        },
    )


def services_list(request):
    services = Service.objects.all().order_by('-is_featured')
    return render(request, "core/services.html", {"services": services})


def news_list(request):
    news = News.objects.all()
    return render(request, "core/news_list.html", {"news_list": news})


def news_detail(request, slug):
    item = get_object_or_404(News, slug=slug)
    return render(request, "core/news_detail.html", {"news": item})


def projects_list(request):
    projects = Project.objects.all()
    return render(request, "core/project_list.html", {"projects": projects})


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            subject = f"رسالة جديدة من {contact.name}"
            body = f"""
                الاسم: {contact.name}
                الهاتف: {contact.phone}
                البريد: {contact.email}
                الخدمة: {contact.get_service_display()}
                الرسالة:
                {contact.message}
                """
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
            messages.success(request, "تم إرسال رسالتك بنجاح.")
            return redirect(reverse("core:contact"))
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"form": form})



def about_us(request):
    return render(request, "core/about_us.html")