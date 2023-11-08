def foo():
    try:
        throwsNumberFormatException()
        throwsUnsupportedDataTypeException()
        throwsFileNotFoundException()
    except Exception as ex:
        if isinstance(ex, FileNotFoundException) or isinstance(ex, NumberFormatException):
            #deal with these two Exceptions without duplicating code
            pass
        elif isinstance(ex, IOException):
            #deal with the UnsupportedDataTypeException as well as any other unchecked IOExceptions
            raise ex