from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        data = response.data.copy()
        response.data.clear()
        response.data['status'] = response.status_code
        response.data['message'] = data
        response.data['id'] = None

    return response
