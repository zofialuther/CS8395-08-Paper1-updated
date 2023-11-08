def main():
    oid_list = ["1.3.6.1.4.1.11.2.17.19.3.4.0.10",
                "1.3.6.1.4.1.11.2.17.5.2.0.79",
                "1.3.6.1.4.1.11.2.17.19.3.4.0.4",
                "1.3.6.1.4.1.11150.3.4.0.1",
                "1.3.6.1.4.1.11.2.17.19.3.4.0.1",
                "1.3.6.1.4.1.11150.3.4.0"]
    sorted_list = sort_oid_list(oid_list)
    for oid in sorted_list:
        print(oid)

def sort_oid_list(oid_list):
    parsed = parse_oid_list(oid_list)
    sorted_list = sorted(parsed, key=lambda x: x[0])
    return [oid[1] for oid in sorted_list]

def parse_oid_list(oid_list):
    parsed = []
    for oid in oid_list:
        numbers = parse_oid(oid)
        parsed.append((numbers, oid))
    return parsed

def parse_oid(oid):
    strings = oid.split(".")
    numbers = [int(s) for s in strings]
    return numbers

main()