def foo():
    try:
        throwsNumberFormatException()
        throwsUnsupportedDataTypeException()
        throwsFileNotFoundException()
    except (FileNotFoundException, NumberFormatException) as ex:
        # deal with these two Exceptions without duplicating code
    except IOException as e:
        # deal with the UnsupportedDataTypeException as well as any other unchecked IOExceptions
        raise e