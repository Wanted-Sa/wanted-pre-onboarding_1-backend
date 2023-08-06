from rest_framework.exceptions import APIException


class RequiredDataException(APIException):
    status_code = 400
    default_detail = 'Required data not found.'
    default_code = 'RequiredDataNotFound'