
class Error(Exception):
    """Base class for exceptions in this module"""
    pass


# Example custom error class extending Exception
class ApiError(Exception):
    def __init__(self, message, exception=None):
        Exception.__init__(self)
        self.status_code = 400
        self.message = message
        self.exception = exception

    def to_dict(self):
        response_body = dict()
        if self.exception is not None:
            response_body["exception"] = self.exception.args
        response_body["message"] = self.message
        return response_body
