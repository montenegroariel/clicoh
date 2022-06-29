import logging

from django.db import IntegrityError
from django.http import JsonResponse
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if isinstance(exc, IntegrityError):
        print(exc)
        err_data = {'Error': 'The stock of the product cannot be a negative number'}
        return JsonResponse(err_data, safe=False, status=503)
    return response
