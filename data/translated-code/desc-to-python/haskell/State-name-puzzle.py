def puzzle(state_names):
    matching_pairs = []
    for state1 in state_names:
        for state2 in state_names:
            if state1 != state2 and state1[:2] == state2[-2:]:
                matching_pairs.append((state1, state2))
    return matching_pairs

def main():
    real_state_names = ["California", "Texas", "New York", "Florida"]
    fake_state_names = ["Califlora", "Texico", "Newida", "Florork"]
    matching_pairs = puzzle(real_state_names + fake_state_names)
    print(matching_pairs)

main()