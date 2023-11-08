def fft(x):
    N = len(x)
    if N <= 1: 
        return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    factor = [exp(-2j * pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + factor[k] for k in range(N // 2)] + \
           [even[k] - factor[k] for k in range(N // 2)]

def main():
    sample_input = [0, 1, 2, 3]
    result = fft(sample_input)
    print(result)

if __name__ == "__main__":
    main()