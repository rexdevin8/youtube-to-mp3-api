from django.urls import path
from stream.audio.views import AudioView

urlpatterns = [
    path('', AudioView.as_view(), name="api-stream"),
]
