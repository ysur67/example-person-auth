from django.urls import path, include
from person.api_views import PersonCreateView
from person.views import RequestResultListView


urlpatterns = [
    path("useradd/", PersonCreateView.as_view(), name="person-add"),
    path("persons/", RequestResultListView.as_view(), name="request-result-list")
]
