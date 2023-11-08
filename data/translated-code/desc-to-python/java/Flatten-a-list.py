class FlattenUtil:
    @staticmethod
    def flatten(input_list):
        flattened_list = []
        for i in input_list:
            if isinstance(i, list):
                flattened_list.extend(FlattenUtil.flatten(i))
            else:
                flattened_list.append(i)
        return flattened_list

    @staticmethod
    def a(*args):
        return list(args)

if __name__ == "__main__":
    treeList = FlattenUtil.a(1, [2, [3, 4], 5, [6, 7, [8, 9]]])
    flattenedList = FlattenUtil.flatten(treeList)
    print(flattenedList)