from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = "events/event_list.html"
    context_object_name = "events"
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.filter(is_published=True).order_start_date()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        qs = self.get_queryset()
        context["upcoming_events"] = qs.filter(start_date__gte=now)
        context["past_events"] = qs.filter(start_date__lt=now).order_by("-start_date")
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"

    def get_queryset(self):
        return Event.objects.filter(is_published=True)
