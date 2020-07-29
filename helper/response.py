from django.http import JsonResponse
from enum import Enum

class ErrorType(Enum):
    class Error:
        def __init__(self, error: str, status_code: int):
            self.error = error
            self.status_code = status_code

    bad_request = Error(error="Bad request", status_code=400)


class ErrorResponse(JsonResponse):
    def __init__(self, error: ErrorType, reason: str):
        error_response = {
            "error": error.value.error,
            "reason": reason
        }
        super(ErrorResponse, self).__init__(error_response, status=error.value.status_code)