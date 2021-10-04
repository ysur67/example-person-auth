from django.views import generic
from person.models import RequestResult


class RequestResultListView(generic.ListView):
    model = RequestResult
    queryset = RequestResult.objects.all()
    template_name = "person/response-list.html"
