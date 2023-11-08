def congruence(congruence_val, input_list, function, output_list):
    modified_input = [x % congruence_val for x in input_list]
    output_list.extend([function(x) for x in modified_input])

def fun_1(x):
    return x**2

def fun_2(x):
    return x*2