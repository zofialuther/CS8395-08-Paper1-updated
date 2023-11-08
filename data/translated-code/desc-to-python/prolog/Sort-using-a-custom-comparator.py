def rosetta_sort(sample_strings):
    def my_comp(s):
        return len(s), s
    
    sorted_list = sorted(sample_strings, key=my_comp)
    print("Original list:", sample_strings)
    print("Sorted list:", sorted_list)

# Example usage
sample_strings = ["apple", "banana", "orange", "kiwi"]
rosetta_sort(sample_strings)