from django.views import generic
from person.models import RequestResult
from person.forms import LoginForm
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy


class LoginTemplateView(generic.TemplateView):
    template_name = "person/login.html"
    form = LoginForm
    
    def post(self, request, *args, **kwargs):
        form: LoginForm = self.form(request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(
            username=form.cleaned_data.get("username", None),
            password=form.cleaned_data.get("password", None)
        )
        login(request, user)
        response = {
            "redirect": reverse_lazy("person:request-result-list")
        }
        return JsonResponse(response, status=status.HTTP_200_OK)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        return context


class RequestResultListView(generic.ListView):
    model = RequestResult
    queryset = RequestResult.objects.all()
    template_name = "person/response-list.html"
