def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def find_index(lst, value):
    return lst.index(value)

def format_table(data):
    max_len = max(len(row) for row in data)
    for row in data:
        print(row.rjust(max_len))

def A131382_terms():
    terms = []
    n = 1
    while True:
        product = 1
        for digit in str(n):
            product *= int(digit)
        digit_sum_product = digit_sum(product)
        if digit_sum_product not in terms:
            terms.append(digit_sum_product)
        else:
            index = find_index(terms, digit_sum_product)
            terms.append(index)
        n += 1
    return terms

A131382 = A131382_terms()
format_table([str(term) for term in A131382[:40]])