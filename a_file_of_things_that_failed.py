#from PIL import pillow

############ EXTEND AND STRIP ############
#strip might not work on lists? 
#used re.sub instead
    # raw_map_split = raw_map_data.split()
    # raw_map_strip = raw_map_data.strip()
    # map_data_clean_.extend(raw_map_split, raw_map_strip)

#why the Fuck is this not valid?
#max_of_map_data = max(map_data_as_int)

    
############ NUMPY EXPERIMENT ############
#ended with an array inside of a list
#would've greatly inconvieniced me later on in the project

#import numpy as np

#map_data = "elevation_small.txt"

#a = np.array([1,2,3,4])
#print(a)

# with open(map_data) as f:
#     map_data_list = []
#     for line in f:
#         map_data_list.append([int(x) for x in line.split()])
    #print(map_data_list)

#print(a.index(3))
#small_map_data = np.loadtxt("elevation_small.txt")
#print(len(small_map_data))
#test = small_map_data[0]
#print(type(test))
#print(test)
#print(map_data_list.index(4068))



############ FOR LOOP TO OBTAIN MAX/MIN VALUES ############
#unneeded due to list formatting 
#failure to iterate int 

# def get_max(map_data_as_int):
#     map_data_for_max = []
#     for _ in map_data_as_int:
#         for lines_for_max in _:
#             map_data_as_int = max(lines_for_max)
#             map_data_for_max.append(map_data_as_int)
#     return map_data_for_max

#map_data_for_max = get_max(map_data_as_int)
