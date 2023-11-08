def prime(n):
    return not bool(re.match(".?|(..+?)\\1+", "?" * n))