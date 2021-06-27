import math


list_x = [1,2,30,-2,5]
list_y = [2,5,20,-1,1]
def get_route(list_x, list_y):
    unvisited = []
    for x,y in zip(list_x,list_y):
        unvisited.append([x,y])

    master_unvisited = unvisited.copy()

    best_dist = -1
    for i in range(len(master_unvisited)):
        # print(i, ' ', '-'*20)
        unvisited = master_unvisited.copy()
        visited = []
        u = unvisited.pop(i)
        visited.append(u)

        while len(unvisited) != 0:
            min_distance = -1
            for idx,cord in enumerate(unvisited):
                dist = math.sqrt(abs(u[0] - cord[0])**2 + abs(u[1] - cord[1])**2)
                if min_distance == -1:
                    min_distance = dist
                    best_node = idx
                if min_distance > dist:
                    min_distance = dist
                    best_node = idx
            u = unvisited.pop(idx)

            visited.append(u)

        # print(visited)
        tot_dist = 0
        for idx in range(len(visited)-1):
            x,y, = visited[idx]
            x1,y1 = visited[idx+1]
            dist = math.sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2)
            tot_dist += dist
        # way back like james
        x,y = visited[0]
        x1, y1 = visited[-1]
        dist = math.sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2)
        tot_dist += dist

        # print(tot_dist, best_dist)

        if best_dist > tot_dist or best_dist == -1:
            best_dist = tot_dist
            best_visited = visited.copy()

    print(best_visited, best_dist)
    return best_visited


