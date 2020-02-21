from rest_framework.exceptions import APIException


class InvalidAction(APIException):
    status_code = 403
    default_detail = "You are already authorized! Please log out firstly to get access to login or registration page!"
    default_code = 'Bad Request'