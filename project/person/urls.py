from django.urls import path, include
from person.api_views import PersonCreateView
from person.views import RequestResultListView, LoginTemplateView


urlpatterns = [
    path("/api/v1/useradd/", PersonCreateView.as_view(), name="person-add"),
    path("login/", LoginTemplateView.as_view(), name="person-login"),
    path("persons/", RequestResultListView.as_view(), name="request-result-list")
]
