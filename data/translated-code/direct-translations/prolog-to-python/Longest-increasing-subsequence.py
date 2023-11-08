def lis(In, Out):
    # we ask Prolog to find the longest sequence
    def one_is(input_list, current, final):
        if not input_list:
            final.extend(current)
        else:
            if not current or current[-1] < input_list[0]:
                one_is(input_list[1:], current + [input_list[0]], final)
            one_is(input_list[1:], current, final)

    sequences = []
    one_is(In, [], sequences)
    max_length = max(len(seq) for seq in sequences)
    longest_sequences = [seq for seq in sequences if len(seq) == max_length]
    Out = longest_sequences

In = [1, 2, 3, 4, 3, 2, 1]
Out = []
lis(In, Out)
print(Out)  # Output: [[1, 2, 3, 4]]