def _menu(items):
    for index, item in enumerate(items):
        print("  %2i) %s" % (index, item))

def _ok(reply, itemcount):
    try:
        n = int(reply)
        return 0 <= n < itemcount
    except:
        return False

def selector(items, prompt):
    'Prompt to select an item from the items'
    if not items: return ''
    reply = -1
    itemcount = len(items)
    while not _ok(reply, itemcount):
        _menu(items)
        reply = input(prompt).strip()
    return items[int(reply)]

if __name__ == '__main__':
    items = ['fee fie', 'huff and puff', 'mirror mirror', 'tick tock']
    item = selector(items, 'Which is from the three pigs: ')
    print("You chose: " + item)