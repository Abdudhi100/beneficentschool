from django.views.generic import DetailView, TemplateView
from .models import SchoolDivision, ProgramPage

class AcademicsIndexView(TemplateView):
    template_name = "academics/academics_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["divisions"] = SchoolDivision.objects.filter(is_published=True)
        context["programs"] = ProgramPage.objects.filter(is_published=True)
        return context

class SchoolDivisionDetailView(DetailView):
    model = SchoolDivision
    template_name = "academics/division_detail.html"
    context_object_name = "division"

    def get_queryset(self):
        return SchoolDivision.objects.filter(is_published=True)

class ProgramPageDetailView(DetailView):
    model = ProgramPage
    template_name = "academics/program_detail.html"
    context_object_name = "program"

    def get_queryset(self):
        return ProgramPage.objects.filter(is_published=True)
