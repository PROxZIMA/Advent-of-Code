import sys, os, time
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.paths_count = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsUtil(self, u, desti, visited, visit_twice, visit_small):
        new_visited = visited.copy()

        if u == desti:
            return 1

        new_visited[u] += 1
        self.paths_count = 0

        for i in self.graph[u]:

            if i.isupper() or (i not in new_visited):
                self.paths_count += self.printAllPathsUtil(
                    i, desti, new_visited, visit_twice, visit_small
                )

            elif (
                visit_twice
                and not visit_small
                and (i in new_visited)
                and new_visited[i] < 2
            ):
                self.paths_count += self.printAllPathsUtil(
                    i, desti, new_visited, visit_twice, True
                )

        return self.paths_count

    def printAllPaths(self, source, desti, visit_twice):
        visited = defaultdict(lambda: 0)
        self.printAllPathsUtil(source, desti, visited, visit_twice, False)

        return self.paths_count


def both_part(data):
    g = Graph()

    for entry in data:
        x, y = entry.split("-")
        if y != "start" and x != "end":
            g.addEdge(x, y)
        if x != "start" and y != "end":
            g.addEdge(y, x)

    return (
        g.printAllPaths("start", "end", False),
        g.printAllPaths("start", "end", True),
    )


def testcase():
    caves_map = (
        open(os.path.join(os.path.dirname(__file__), "day-12-test.txt"))
        .read()
        .split("\n")
    )

    assert both_part(caves_map) == (10, 36)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        testcase()

    caves_map = (
        open(os.path.join(os.path.dirname(__file__), "day-12-input.txt"))
        .read()
        .split("\n")
    )

    s = time.perf_counter()
    print("Part 1: {0}\nPart 2: {1}".format(*both_part(caves_map)))
    print(f"> {os.path.basename(__file__)} {round(time.perf_counter() - s, 7)} secs\n")
