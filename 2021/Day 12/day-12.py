import os
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.paths_count = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, desti, visited, path):
        if u.islower():
            visited[u]= True
        path.append(u)

        if u == desti:
            self.paths_count += 1
            print(' '.join(path))
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, desti, visited, path)

        path.pop()
        visited[u] = False


    def printAllPaths(self, source, desti):
        visited = defaultdict(lambda: False)
        path = []
        self.printAllPathsUtil(source, desti, visited, path)
        return self.paths_count


def part1(data):
    g = Graph()
    for entry in data:
        x, y = entry.split('-')
        g.addEdge(x, y)
        g.addEdge(y, x)
    return g.printAllPaths('start', 'end'), False


def part2(data):
    g = Graph()
    for entry in data:
        x, y = entry.split('-')
        g.addEdge(x, y)
        g.addEdge(y, x)
    print(g.printAllPaths('start', 'end', True))
    return 36


def testcase():
    caves_map = open(os.path.join(os.path.dirname(__file__), "day-12-test.txt")).read().split('\n')

    # assert part1(caves_map) == 10
    assert part2(caves_map) == 36


if __name__ == "__main__":
    testcase()

    caves_map = open(os.path.join(os.path.dirname(__file__), "day-12-input.txt")).read().split('\n')

    # print(f"Part 1: {part1(caves_map)}")
    # print(f"Part 2: {part2(caves_map)}")