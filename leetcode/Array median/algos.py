from collections import deque


def binary_search(arr, f):
    l = len(arr)

    left, right = 0, l-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == f:
            return f
        elif arr[mid] > f:
            right = mid - 1
        else:
            left = mid + 1

    return None
    

def depth_first_search_recursion(graph, parents, visited, curr, end=None):
    
    if curr == end:
        return True
    
    for neighbour in graph[curr]:
        if neighbour not in visited:
            visited.add(neighbour)
            parents[neighbour] = curr
            if depth_first_search_recursion(graph, parents, visited, neighbour, end):
                return True

    return False

def depth_first_search(graph, start, end=None):

    parents = {start: None}
    visited = set([start])

    depth_first_search_recursion(graph, parents, visited, start, end)

    print("Connected vertices: ", visited)
    print("Vertices parents: ", parents)


def breadth_first_search(graph, start, end=None):
    
    queue = deque([start])
    parents = {start: None}
    visited = set([start])

    while queue:
        curr = queue.popleft()

        if curr == end:
            break

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = curr
                queue.append(neighbor)

    print("Connected vertices: ", visited)
    print("Vertices parents: ", parents)

    path = []
    
    if end in parents:
        curr = end
        while curr is not None:
            path.append(curr)
            curr = parents[curr]
        
        path.reverse()

    if end and not path:
        print(f"No path found between {start} and {end}")
    else:
        print("Path:", path)

def main():
    # A = [0,1,2,3,4,5]
    # f = 0

    # found = binary_search(A, f)
    # print("found this -> " + str(found))

    graph = [[1,2],[0,3],[0,3],[1,2]]

    breadth_first_search(graph, 0, 3)
    depth_first_search(graph, 0, 3)
    


if __name__ == "__main__":
    main()

