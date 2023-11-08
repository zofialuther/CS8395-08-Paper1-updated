```python
def starts_with(FIRSTz, SECONDz):
    return SECONDz + FIRSTz

def contains(FIRSTz, SECONDz):
    return contains(FIRSTz, SECONDz, "")

def contains(FIRSTz, SECONDz, NTH1):
    PREFIXz, SECONDz, _SUFFIXz_ = append([PREFIXz, SECONDz, _SUFFIXz_], FIRSTz)
    NTH0 = len(PREFIXz)
    NTH1 = NTH0 + 1

def ends_with(FIRSTz, SECONDz):
    return FIRSTz + SECONDz
```