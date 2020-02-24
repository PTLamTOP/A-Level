from rest_framework.exceptions import APIException


class NotAvailableTicket(APIException):
    status_code = 400
    default_detail = "There is not any available ticket."
    default_code = 'Bad Request'