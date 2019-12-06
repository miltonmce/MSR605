
class MSRException(Exception):
    """ Common base class for all non-exit exceptions. """

    def __init__(self,msj):  # real signature unknown
        Exception.__init__(self,msj)

    @staticmethod  # known case of __new__
    def __new__(S, *more):  # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """


class ReadError(MSRException):
    pass


class ReadWriteError(MSRException):
    pass


class CommandFormatError(MSRException):
    pass


class InvalidCommand(MSRException):
    pass


class InvalidCardSwipeForWrite(MSRException):
    pass


class SetError(MSRException):
    pass