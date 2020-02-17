from rest_framework.exceptions import APIException


class NotAllowedData(APIException):
    status_code = 400
    default_detail = "Standard user can create a card only with status 'NEW'" \
                     "and update 'text' and 'status' field. Admin can update only 'text', " \
                     "'status' and 'executor' fields."
    default_code = 'not allowed data'


class NotAllowedStatus(APIException):
    status_code = 400
    default_detail = "Standard user can change status from 'IP' <-> 'RD'." \
                     "Admin can can from 'RD' <-> 'DN'."
    default_code = 'not allowed data'


class NotAllowedMethod(APIException):
    status_code = 400
    default_detail = "Standard user can not delete object."
    default_code = 'not allowed method'