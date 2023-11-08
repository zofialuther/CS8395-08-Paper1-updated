data = [
    '1.3.6.1.4.1.11.2.17.19.3.4.0.10',
    '1.3.6.1.4.1.11.2.17.5.2.0.79',
    '1.3.6.1.4.1.11.2.17.19.3.4.0.4',
    '1.3.6.1.4.1.11150.3.4.0.1',
    '1.3.6.1.4.1.11.2.17.19.3.4.0.1',
    '1.3.6.1.4.1.11150.3.4.0'
]

for s in sorted(data, key=lambda x: list(map(int, x.split('.'))):
    print(s)