from rest_framework.exceptions import APIException


class NotAllowedToUpdate(APIException):
    status_code = 400
    default_detail = "The hall can not be updated, as a ticket was already purchased for a hall's session!"
    default_code = 'Bad Request'