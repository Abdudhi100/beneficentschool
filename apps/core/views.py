from django.views.generic import DetailView, TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import StaticPage, HomepageHero, FeatureCard, FAQ, ContactMessage
from apps.testimonials.models import Testimonial


class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heroes"] = HomepageHero.objects.filter(is_active=True)
        context["features"] = FeatureCard.objects.filter(is_active=True)
        context["testimonials"] = Testimonial.objects.filter(is_published=True)[:6]
        return context


class StaticPageDetailView(DetailView):
    model = StaticPage
    template_name = "core/static_page.html"
    context_object_name = "page"


class AboutView(TemplateView):
    template_name = "core/about.html"


class FAQListView(ListView):
    model = FAQ
    template_name = "core/faq.html"
    context_object_name = "faqs"

    def get_queryset(self):
        return FAQ.objects.filter(is_active=True)


class ContactView(CreateView):
    model = ContactMessage
    template_name = "core/contact.html"
    fields = ["name", "email", "phone", "subject", "message"]
    success_url = reverse_lazy("core:contact")

    def form_valid(self, form):
        messages.success(self.request, "Thank you for getting in touch! We will get back to you shortly.")
        return super().form_valid(form)