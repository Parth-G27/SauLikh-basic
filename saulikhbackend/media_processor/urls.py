from django.urls import path
from .views import FileUploadView, ExtractedTextListView

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('texts/', ExtractedTextListView.as_view(), name='extracted-text-list'),
]
