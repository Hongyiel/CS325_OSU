# BFS algorithm in Python
# https://www.programiz.com/dsa/graph-bfs

import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    # what is deque 
    # https://excelsior-cjh.tistory.com/96#:~:text=1.%20deque%EB%9E%80,%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0%EB%A5%BC%20%EC%9D%98%EB%AF%B8%ED%95%9C%EB%8B%A4.&text=python%20%EC%97%90%EC%84%9C%20collections.deque%20%EB%8A%94%20list%20%EC%99%80%20%EB%B9%84%EC%8A%B7%ED%95%98%EB%8B%A4.
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
