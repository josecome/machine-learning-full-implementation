from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views as api_views

urlpatterns = [
    path('process-request/', api_views.ProcessRequest.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)