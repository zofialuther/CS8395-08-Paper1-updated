def strdup(InputString, OutputString):
    CString = c_malloc(100)
    c_strcpy(CString, InputString)
    c_assign_string(OutputString, CString)