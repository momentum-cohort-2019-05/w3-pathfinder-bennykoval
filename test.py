from PIL import pillow

import re

map_data = "elevation_small.txt"

with open(map_data) as f:
    raw_map_data = f.readlines()

def clean_text(raw_map_data):
    map_data_clean_ = []
    for _ in raw_map_data:
        raw_map_clean = re.sub(r'[^0-9 ]', '', _).split()
        map_data_clean_.append(raw_map_clean)
    return map_data_clean_

def str_to_int(map_data_pre_int):
    map_data_as_int = []
    for _ in map_data_pre_int:
        for lines_in_map_data in _:
            map_data_pre_int = int(lines_in_map_data)
            map_data_as_int.append(map_data_pre_int)
    return map_data_as_int

# def get_max(map_data_as_int):
#     map_data_for_max = []
#     for _ in map_data_as_int:
#         for lines_for_max in _:
#             map_data_as_int = max(lines_for_max)
#             map_data_for_max.append(map_data_as_int)
#     return map_data_for_max
# wow this was so unneeded!


map_data_pre_int = clean_text(raw_map_data)

map_data_as_int = str_to_int(map_data_pre_int)

#map_data_for_max = get_max(map_data_as_int)

max_of_map_data = (max(map_data_as_int))

min_of_map_data = (min(map_data_as_int))

print(min_of_map_data)
