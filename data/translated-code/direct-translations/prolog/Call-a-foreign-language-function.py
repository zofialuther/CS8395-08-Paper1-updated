import ctypes

plffi = ctypes.CDLL('plffi')

def strdup(string):
    strdup = plffi.strdup
    strdup.argtypes = [ctypes.c_char_p]
    strdup.restype = ctypes.c_char_p
    return strdup(string)