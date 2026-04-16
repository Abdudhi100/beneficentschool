from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages

from .models import AdmissionPage, AdmissionStep, AdmissionRequirement, AdmissionFAQ, AdmissionInquiry
from .forms import AdmissionInquiryForm


class AdmissionsIndexView(CreateView):
    model = AdmissionInquiry
    form_class = AdmissionInquiryForm
    template_name = "admissions/admissions_index.html"
    success_url = reverse_lazy("admissions:index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the active admission page content (assuming only one is published)
        context["page_content"] = AdmissionPage.objects.filter(is_published=True).first()
        context["steps"] = AdmissionStep.objects.filter(is_active=True)
        context["requirements"] = AdmissionRequirement.objects.filter(is_active=True)
        context["faqs"] = AdmissionFAQ.objects.filter(is_active=True)
        return context

    def form_valid(self, form):
        messages.success(self.request, "Your admission inquiry has been received. Our team will contact you shortly!")
        return super().form_valid(form)
