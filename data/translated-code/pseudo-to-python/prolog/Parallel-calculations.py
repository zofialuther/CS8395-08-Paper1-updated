```python
import threading

def threaded_decomp(Number, ID):
    t = threading.Thread(target=prime_decomp, args=(Number, Y,))
    t.start()
    t.join()
    return (Number, Y)

def threaded_decomp_list(List, Erg):
    IDs = []
    for num in List:
        t = threading.Thread(target=threaded_decomp, args=(num, IDs,))
        t.start()
        IDs.append(t)
    for t in IDs:
        t.join()
    Results = [t for t in IDs]
    Smallest_Factors_List = [pack_exit_out(t) for t in Results]
    return largest_min_factor(Smallest_Factors_List, Erg)

def pack_exit_out(exited):
    return exited

def largest_min_factor(factor_list, erg):
    if factor_list:
        N, Facs = factor_list[0]
        MF = min(Facs)
        return largest_min_factor(factor_list[1:], (N, MF, Facs), erg)
    else:
        return erg

def format_it(List):
    Number, Factors = threaded_decomp_list(List, (Number, Factors))
    print('Number with largest minimal Factor is', Number)
    print('Factors are', Factors)
```