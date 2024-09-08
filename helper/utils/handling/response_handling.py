from ..keys.response_keys import MESSAGE, STATUS, DATA, ERROR_DETAILS

class ResponseHandling:
    @staticmethod
    def failure_response_message(status, message, error_details):
        """
        Constructs a response dictionary for failure cases.
        
        :param status: Status code or message indicating the failure condition.
        :param message: A descriptive message explaining the failure.
        :param error_details: Additional details about the error.
        :returns: Dictionary containing the failure response with status, message, and error details.
        """
        if error_details is None:
            return {STATUS: status, MESSAGE: message}
        return {STATUS: status, MESSAGE: message, ERROR_DETAILS: error_details}

    @staticmethod
    def success_response_message(status, message, data):
        """
        Constructs a response dictionary for successful cases.
        
        :param status: Status code or message indicating the success condition.
        :param message: A descriptive message explaining the success.
        :param data: The data to be included in the success response.
        :returns: Dictionary containing the success response with status, message, and data.
        """
        if data is None:
            return {STATUS: status, MESSAGE: message}
        return {STATUS: status, MESSAGE: message, DATA: data}
