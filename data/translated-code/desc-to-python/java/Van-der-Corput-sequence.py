```python
class VanDerCorput:
    def vdc(self, n):
        vdc_sequence = 0
        while n:
            n, d = divmod(n, 2)
            vdc_sequence += d / 2
        return vdc_sequence

if __name__ == "__main__":
    vdc_generator = VanDerCorput()
    for i in range(11):
        print(vdc_generator.vdc(i))
```