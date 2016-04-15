# -*- coding = utf-8 -*-


class Node():

    def __init__(self, name):
        self.name = name
        self.sub_directories = []

    def split_path(self, path):
        dir_name = [0] * 2
        path = path[1::]
        index = path.find("/")
        # print(path, index)
        if index == -1:
            dir_name[0] = path
            dir_name[1] = None
        else:
            dir_name[0] = path[0:index]
            dir_name[1] = path[index::]
        return dir_name

    def mkdir(self, path):
        if path is None:
            return 0
        # print(type(path))
        current_path_status = self.split_path(path)
        for directory in self.sub_directories:
            if directory.name == current_path_status[0]:
                return directory.mkdir(current_path_status[1])
        node = Node(current_path_status[0])
        self.sub_directories.append(node)
        return 1 + node.mkdir(current_path_status[1])


with open("A-large-practice.in", "r") as fin, open("large_out.out", "w") as fout:
    T = int(fin.readline().strip())
    for i in range(1, T + 1):
        N, M = ([int(x) for x in fin.readline().strip().split()])
        root = Node("")
        for j in range(N):
            path = fin.readline().strip()
            root.mkdir(path)
        counter = 0
        for j in range(M):
            path = fin.readline().strip()
            counter += root.mkdir(path)
        fout.write("Case #{}: {}\n".format(i, counter))
    print("done")
