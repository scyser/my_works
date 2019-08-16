# find the best way for data from txt file

def find_best_way(file_name, first_point, last_point):
    import math
    with open(file_name, "r") as file:
        file_list = file.readlines()
        new_list = [file_list[i].rstrip().split(" ") for i in range(len(file_list))]
        size_matrix = int(new_list.pop([0][0])[0])
        for i in range(len(new_list)-size_matrix):
            new_list.pop()
        main_dict = {route[0]: {route[1]: float(route[2])} for route in new_list}
        main_dict2 = {route[1]: {route[0]: float(route[2])} for route in new_list if route[1] not in main_dict}
        main_dict.update(main_dict2)
        for route in new_list:
            main_dict[route[0]].update({route[1]: float(route[2])})
            main_dict[route[1]].update({route[0]: float(route[2])})

        weight_list = {key: math.inf for key in main_dict}
        weight_list[first_point] = 0

        visited_cities = []

        for i in range(len(weight_list)):
            if i == 0:
                first_city = first_point

            for second_city in main_dict.get(first_city):
                if (main_dict.get(first_city).get(second_city) + weight_list[first_city]) <= weight_list[second_city]:
                    weight_list[second_city] = main_dict.get(first_city).get(second_city) + weight_list[first_city]
                elif weight_list[first_city] > main_dict.get(first_city).get(second_city) + weight_list[second_city]:
                    weight_list[first_city] = main_dict.get(first_city).get(second_city) + weight_list[second_city]

            if first_city not in visited_cities:
                visited_cities.append(first_city)

            min_weight_city = math.inf
            for second_city in main_dict.get(first_city):
                if (second_city not in visited_cities)and (weight_list[second_city] < min_weight_city):
                    min_weight_city = weight_list[second_city]
                    next_city = second_city

            if next_city == first_city:
                min_weight_city = math.inf
                for second_city in main_dict.get(visited_cities[0]):
                    if (second_city not in visited_cities) and (weight_list[second_city] < min_weight_city):
                        min_weight_city = weight_list[second_city]
                        next_city = second_city

            first_city = next_city

        best_way = []
        best_way.append(last_point)

        while last_point != first_point:
            min_weight_city = math.inf
            next_point = last_point
            for second_city in main_dict.get(next_point):
                if weight_list[second_city] < min_weight_city:
                    if second_city == first_point and weight_list[next_point] != main_dict.get(next_point).get(
                            second_city):
                        continue
                    else:
                        min_weight_city = weight_list[second_city]
                        last_point = second_city
            best_way.append(last_point)
        best_way = best_way[::-1]
    return best_way, weight_list[best_way[-1]]

best_way, weight_way = find_best_way("testing.txt", "1", "12")
print("Лучший путь", best_way)
print("Дальность пути", weight_way)

