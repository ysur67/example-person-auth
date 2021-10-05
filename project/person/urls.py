from django.urls import path, include
from person.api_views import PersonCreateView, TxtDownloadFileView, XlsxDownloadFileView
from person.views import RequestResultListView, LoginTemplateView

app_name = "person"
urlpatterns = [
    path("api/v1/", include([
        path("useradd/", PersonCreateView.as_view(), name="person-add"),
        path("download-txt/", TxtDownloadFileView.as_view(), name="txt-download"),
        path("download-xlsx/", XlsxDownloadFileView.as_view(), name="xlsx-download"),
    ])),
    path("login/", LoginTemplateView.as_view(), name="person-login"),
    path("results/", RequestResultListView.as_view(), name="request-result-list"),
]
