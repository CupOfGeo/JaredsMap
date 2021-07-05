import googlemaps
import os

# Get environment variables
api_key = os.getenv('GOOGLE_API')

# with open('secret.txt', 'r') as file:
#     api_key = file.read()

gmaps = googlemaps.Client(key=api_key)


# # Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
#
# # Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

def do_the_thing(origin, destination, big_dic):
    directions_result = gmaps.distance_matrix(origin, destination, mode="driving")
    for idx, thing in enumerate(directions_result['rows']):
        for idx2, d in enumerate(thing['elements']):
            # print(origin[idx], '->', destination[idx2], d['distance']['value'])
            big_dic[origin[idx] + '|' + destination[idx2]] = d['distance']['value']
        # print('-' * 50)
    return big_dic


# Request directions via public transit
lis = ["Hewlett, NY", "Lynbrook, NY", "Long Beach, NY", 'Valley Stream, NY', "Lawrence, Ny", 'Island park, ny',
       'far rockaway, ny', 'Inwood, NY', 'Woodmere, Ny', 'oceanside, ny', 'Rockville center, ny', 'atlantic beach, ny']


# now = datetime.now()
def make_distance_matrix(lis):
    if len(lis) > 20:
        print('Too many locations')
        return {}
    elif len(lis) > 10:
        big_dic = {}
        # quad 1
        big_dic = do_the_thing(lis[:10], lis[:10], big_dic)

        big_dic = do_the_thing(lis[:10], lis[10:], big_dic)

        big_dic = do_the_thing(lis[10:], lis[:10], big_dic)

        big_dic = do_the_thing(lis[10:], lis[10:], big_dic)

    else:
        # directions_result = gmaps.distance_matrix(lis,lis,mode="driving")
        big_dic = {}
        # quad 1
        big_dic = do_the_thing(lis, lis, big_dic)
    # print(len(big_dic))
    return big_dic


# departure_time=now)
# print(directions_result)
# print('+'*50)


# print(big_dic)


# big_dic = parse_results(directions_result, {})
# big_dic = (directions_result, {})
import math


def get_route(master_arr, list):
    if master_arr == {}:
        return []
    start = list[0]

    master_unvisited = list.copy()

    best_dist = -1
    # try from every start
    for i in range(len(master_unvisited)):

        unvisited = master_unvisited.copy()
        visited = []
        u = unvisited.pop(i)
        visited.append(u)

        while len(unvisited) != 0:
            min_distance = -1
            for idx, cord in enumerate(unvisited):
                key = u + '|' + unvisited[idx]
                dist = master_arr[key]
                if min_distance == -1:
                    min_distance = dist
                    best_node = idx
                elif min_distance > dist:
                    min_distance = dist
                    best_node = idx
            u = unvisited.pop(best_node)
            visited.append(u)

        # calculate total distance
        tot_dist = 0
        for idx in range(len(visited) - 1):
            key = visited[idx] + '|' + visited[idx + 1]
            dist = master_arr[key]
            tot_dist += dist

        # way back like james (way back home counts
        key = visited[0] + "|" + visited[-1]
        dist = master_arr[key]
        tot_dist += dist
        # finish tot_dist calc

        #print(visited, tot_dist)
        if best_dist > tot_dist or best_dist == -1:
            best_dist = tot_dist
            best_visited = visited.copy()

    s_idx = best_visited.index(start)
    out_route = best_visited[s_idx:] + best_visited[:s_idx]
    out_route = out_route[::-1]
    #print(out_route, best_dist)
    # print(master_arr.items())
    return out_route


def one_shot_url(list_of_addys):
    big_dic = make_distance_matrix(list_of_addys)
    addy_list = get_route(big_dic, list_of_addys)
    return addy_list
    # base_url = 'https://www.google.com/maps/dir/'
    # url = ''
    # for addy in addy_list:
    #     url += "+".join(addy.split(' ')) + '/'
    # return base_url + url


#print(one_shot_url(lis))
