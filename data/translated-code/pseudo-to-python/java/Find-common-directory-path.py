def commonPath(paths):
    commonPath = ""
    folders = [None] * len(paths)

    for i in range(len(paths)):
        folders[i] = paths[i].split("/")

    for j in range(len(folders[0])):
        s = folders[0][j]
        for i in range(1, len(paths)):
            if s != folders[i][j]:
                return commonPath
        commonPath += s + "/"

    return commonPath