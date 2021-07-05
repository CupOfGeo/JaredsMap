import math

def get_route(list_x, list_y):
    assert len(list_x) == len(list_y)

    # the memory table so that it only has to do this distance calculations once between points
    # master_arr['loc1,loc2'] = distance
    master_arr = {}

    unvisited = []
    for x, y in zip(list_x, list_y):
        unvisited.append([x, y])

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
            for idx, cord in enumerate(unvisited):
                # dist = math.sqrt(abs(u[0] - cord[0])**2 + abs(u[1] - cord[1])**2)
                # picking loc1 < loc2 so order is kept 'loc1,loc2'
                # so that you don't get 'loc2,loc1'
                if u[0] <= cord[0]:
                    key = str(u[0]) + ',' + str(u[1]) + ',' + str(cord[0]) + ',' + str(cord[1])
                else:
                    key = str(cord[0]) + ',' + str(cord[1]) + ',' + str(u[0]) + ',' + str(u[1])

                if key in master_arr.keys():
                    dist = master_arr[key]
                else:
                    master_arr[key] = math.sqrt(abs(u[0] - cord[0]) ** 2 + abs(u[1] - cord[1]) ** 2)
                    dist = master_arr[key]
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
        for idx in range(len(visited) - 1):
            x, y, = visited[idx]
            x1, y1 = visited[idx + 1]

            if x <= x1:
                key = str(x) + ',' + str(y) + ',' + str(x1) + ',' + str(y1)
            else:
                key = str(x1) + ',' + str(y1) + ',' + str(x) + ',' + str(y)

            if key in master_arr.keys():
                dist = master_arr[key]
            else:
                master_arr[key] = math.sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2)
                dist = master_arr[key]

            tot_dist += dist

        # way back like james
        x, y = visited[0]
        x1, y1 = visited[-1]
        if x <= x1:
            key = str(x) + ',' + str(y) + ',' + str(x1) + ',' + str(y1)
        else:
            key = str(x1) + ',' + str(y1) + ',' + str(x) + ',' + str(y)

        if key in master_arr.keys():
            dist = master_arr[key]
        else:
            master_arr[key] = math.sqrt(abs(x - x1) ** 2 + abs(y - y1) ** 2)
            dist = master_arr[key]
        tot_dist += dist

        # print(tot_dist, best_dist)

        if best_dist > tot_dist or best_dist == -1:
            best_dist = tot_dist
            best_visited = visited.copy()

    print(best_visited, best_dist)
    print(master_arr.items())
    return best_visited
