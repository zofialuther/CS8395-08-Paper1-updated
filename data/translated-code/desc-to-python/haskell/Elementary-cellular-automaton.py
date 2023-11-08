def rule(n, l, x, r):
    result = (l ** x) / r % n
    return result

def initial(lst, n):
    diff = n - len(lst)
    left_pad = diff // 2
    right_pad = diff - left_pad
    padded_lst = [0] * left_pad + lst + [0] * right_pad
    final_lst = padded_lst[-left_pad:] + padded_lst + padded_lst[:right_pad]
    return final_lst