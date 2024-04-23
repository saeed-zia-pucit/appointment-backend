from rest_framework.response import Response
from rest_framework import status

class StandardResponse:
    # SuccessMessageKey = 'SuccessMessage'
    @classmethod
    def success(cls,successMessage, data=None,status_code=status.HTTP_200_OK):
        response_data = {
            "data": {
            'SuccessMessage':successMessage,
            **data  # Unpack any provided data into the "data" object
            }
    }
        return Response(response_data, status=status_code)

    @classmethod
    def created(cls,successMessage, data):
        response_data = {
            "data": {
            "SuccessMessage":successMessage,
            **data  # Unpack any provided data into the "data" object
            }
    }
        return Response(response_data, status=status.HTTP_201_CREATED)

    @classmethod
    def error(cls,error_message, status_code=status.HTTP_400_BAD_REQUEST):
  
        response_data = {
            "data": {
               'errorMessage': error_message
            }
    }
        return Response(response_data, status=status_code)