```python
def selection_sort(input_list, output_list):
    if not input_list:
        return []
    else:
        h = input_list[0]
        l = input_list[1:]
        h1, l2 = exchange(h, l)
        l1 = selection_sort(l2, [])
        output_list.append(h1)
        output_list.extend(l1)
        return output_list

def exchange(h, l):
    if not l:
        return h, []
    else:
        h2 = min(l)
        if h < h2:
            return h, l
        else:
            index = l.index(h2)
            l1 = l[:]
            l1[index] = h
            l2 = l1[:]
            l2[index] = h2
            return h2, l1
```