from rest_framework import status
from rest_framework.exceptions import APIException


class YouHaveAlreadyRatedError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "You've already rated this article"
    default_code = "bad_request"