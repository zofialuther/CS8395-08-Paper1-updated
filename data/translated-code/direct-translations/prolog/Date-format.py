def display_date():
    Time = get_time()
    Short = format_time('%Y-%M-%d', Time)
    Long = format_time('%A, %B %d, %Y', Time)
    print(Short)
    print(Long)