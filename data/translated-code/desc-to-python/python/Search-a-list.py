haystack = ["apple", "orange", "banana", "Washington", "grape", "Bush"]
search_terms = ["Washington", "Bush"]

for term in search_terms:
    if term in haystack:
        print(f"{term} found at index {haystack.index(term)}")
    else:
        print(f"{term} not found in haystack list")