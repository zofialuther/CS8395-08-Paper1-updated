def commonPrefix2(list1, list2):
    if not list1 or not list2:
        return []
    if list1[0] == list2[0]:
        return [list1[0]] + commonPrefix2(list1[1:], list2[1:])
    else:
        return []

def commonPrefix(listOfLists):
    if not listOfLists:
        return []
    prefix = listOfLists[0]
    for lst in listOfLists[1:]:
        prefix = commonPrefix2(prefix, lst)
    return prefix

def splitPath(string):
    return string.split('/')

def commonDirPath(listOfPaths):
    paths = list(map(splitPath, listOfPaths))
    return commonPrefix(paths)

def main():
    paths = [
        "/home/user1/tmp/coverage/test",
        "/home/user1/tmp/covert/operator",
        "/home/user1/tmp/coven/members"
    ]
    result = commonDirPath(paths)
    print(result)

main()