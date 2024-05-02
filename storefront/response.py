from rest_framework.response import Response
from rest_framework import status

class StandardResponse:
    @classmethod
    def success(cls, success_message, data=None, status_code=status.HTTP_200_OK):
        response_data = {"SuccessMessage": success_message}
        if data:
            response_data.update(data)
        return Response({"data": response_data}, status=status_code)

    @classmethod
    def created(cls, success_message, data=None):
        response_data = {"SuccessMessage": success_message}
        if data:
            response_data.update(data)
        return Response({"data": response_data}, status=status.HTTP_201_CREATED)

    @classmethod
    def error(cls, error_message, status_code=status.HTTP_400_BAD_REQUEST):
        return Response({"data": {"errorMessage": error_message}}, status=status_code)