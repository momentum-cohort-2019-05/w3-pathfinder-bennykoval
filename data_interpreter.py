import re

map_data = "elevation_small.txt"

with open(map_data) as f:
    raw_map_data = f.readlines()

def clean_text(raw_map_data):
    """Keep only spaces and numbers in map_data"""
    map_data_clean_ = []
    for _ in raw_map_data:
        raw_map_clean = re.sub(r'[^0-9 ]', '', _).split()
        map_data_clean_.append(raw_map_clean)
    return map_data_clean_

def str_to_int(map_data_pre_int):
    """Convert all strings to integers in map_data"""
    map_data_as_int = []
    for _ in map_data_pre_int:
        for lines_in_map_data in _:
            map_data_pre_int = int(lines_in_map_data)
            map_data_as_int.append(map_data_pre_int)
    return map_data_as_int

def max_of_data(map_data_as_int):
    """Placeholder for max, min, and range of map data, as well as variable dec for shades of grey"""
    max_of_map_data = max(map_data_as_int)
    return max_of_map_data
    
def min_of_data(map_data_as_int):
    min_of_map_data = min(map_data_as_int)
    return min_of_map_data

def range_of_data(map_data_as_int):
    range_of_map_data = max(map_data_as_int) - min(map_data_as_int)
    return range_of_map_data
    
def shades_grey():
    shades_of_grey = 255
    return shades_of_grey

def shade_at_elevation(map_data_as_int, min_of_map_data, range_of_map_data, shades_of_grey):
    """For each elevation, return a shade"""
    # first_list_of_elevation = []
    # for line in map_data_as_int:
    second_list_of_elevation = []
    for elevation in map_data_as_int:
        second_list_of_elevation.append(int((elevation - min_of_map_data) / (range_of_map_data / shades_of_grey)))
        # second_list_of_elevation.append(int((elevation - 3139) / (2509 / 255)))
        #first_list_of_elevation.append(second_list_of_elevation)
    return second_list_of_elevation

clean_boy = clean_text(raw_map_data)
map_data_as_int_list = str_to_int(clean_boy)
highest_elevation = max_of_data(map_data_as_int_list)
lowest_elevation = min_of_data(map_data_as_int_list)
range_elevation = range_of_data(map_data_as_int_list)
shades_on_shades = shades_grey()
cheap_sunglasses_indoors = shade_at_elevation(map_data_as_int_list, lowest_elevation, range_elevation, shades_on_shades)