def bfs(graph, start, goal):
    visited = set()
    queue = []

    queue.append(start)
    visited.add(start)

    parent_node = dict()
    parent_node[start] = None

    path_found = False
    while queue:
        current_node = queue[0]
        if current_node == goal:
            path_found = True
            break
        
        for node in graph[current_node]:
            if node not in visited:
                queue.append(node)
                visited.add(node)
                parent_node[node] = current_node
        queue.pop(0) 
    
    if path_found:
        path = list()
        current_node = goal
        path.append(current_node)
        while current_node != start:
            path.append(parent_node[current_node])
            current_node = parent_node[current_node]
        path.reverse()
        return path
    return -1
