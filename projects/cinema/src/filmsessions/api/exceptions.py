from rest_framework.exceptions import APIException


class InvalidSessionTime(APIException):
    status_code = 400
    default_detail = "The session's start time is less/equal than end time OR " \
                     "session's time is out of film's screening time!"
    default_code = 'Bad Request'


class NotAvailableTime(APIException):
    status_code = 400
    default_detail = "There is already a session during this time in the same hall!"
    default_code = 'Bad Request'


class NotAllowedToUpdate(APIException):
    status_code = 400
    default_detail = "The session can not be updated, as a ticket was already purchased for the session!"
    default_code = 'Bad Request'
