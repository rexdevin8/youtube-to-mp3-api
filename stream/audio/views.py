from rest_framework.views import APIView
from rest_framework.schemas import ManualSchema, AutoSchema
from rest_framework import permissions

from django.http import JsonResponse
from .audio_stream import AudioStream
from helper.response import ErrorResponse, ErrorType

permission = permissions.AllowAny

class AudioView(APIView):
    permission_classes = (permission,)

    def get(self, request):
        youtube_url = request.GET.get('url', None)
        (response, error) = self.handle_youtube_url(youtube_url)
        if error is not None:
            return error
        return JsonResponse(response)

    def handle_youtube_url(self, url:str) -> (dict, ErrorResponse):
        if url is None:
            error_response = ErrorResponse(
                error=ErrorType.bad_request,
                reason="url(youtube) is not found. The url must be in this format `<heroku_app>.herokuapp.com/?url=<youtube_url>`"
            )
            return (None, error_response)
        stream = AudioStream(youtube_url=url)
        video_info = stream.info()
        if not isinstance(video_info, AudioStream._Audio):
            error_response = ErrorResponse(
                error=ErrorType.bad_request,
                reason="url(youtube) could not be verified."
            )
            return (None, error_response)
        return (video_info.toJSON(), None)

