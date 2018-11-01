

class ApiBaseException(Exception):

    def __init__(self, message='服务器发生未知错误', code=300):
        self.code = code
        self.message = message
        super(ApiBaseException, self).__init__(message)


class InvalidCodeException(ApiBaseException):
    def __init__(self, message='验证码错误或失效', code=300, ):
        self.code = code
        self.message = message


class ExistedException(ApiBaseException):
    pass


class ForbiddenException(ApiBaseException):
    pass


class NotFoundException(ApiBaseException):
    pass


class NetWorkException(ApiBaseException):
    def __init__(self, message='网络连接异常', code=300, ):
        self.code = code
        self.message = message


class WrongTypeException(ApiBaseException):
    def __init__(self, message='格式错误', code=300):
        self.code = code
        self.message = message


class TradeException(ApiBaseException):
    def __init__(self, message='交易失败', code=300):
        self.code = code
        self.message = message
