def transform(s, copyList):
    transformation = scale(s, s) + rotate(36) + foldMap(copyList, copy, [0, 72, 144, 216, 288])
    return transformation