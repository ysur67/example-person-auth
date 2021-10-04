from django.urls import path, include
from person.views import PersonCreateView

urlpatterns = [
    path("useradd/", PersonCreateView.as_view(), name="person-add")
]
