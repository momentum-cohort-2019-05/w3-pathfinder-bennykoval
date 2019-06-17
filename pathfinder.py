from data_interpreter import *
from PIL import Image, ImageDraw

img_width = 600
img_height = 600

#list 1 = long_list[:600]
#list 2 = long_list[601:1200] ugh shit never mind i would have to do this like 600 times

# elevation_scheme = (range_of_map_data * 255)
def list_of_lists(map_as_int_list):
    low_moan = []
    x = 0 
    for x in range(600):
        y = 0
        high_scream = []
        for y in range(600):
            high_scream.append(map_as_int_list[x + 600 * y])
        low_moan.append(high_scream)
    return low_moan

def draw_map(low_moan):
    empty_map = Image.new(mode="L", size=(img_width, img_height))
    empty_map.save('mappy_map.png')
    not_empty_map = ImageDraw.Draw(empty_map)
    y = 0 
    for line in low_moan:
        x = 0
        for elevation in line:
            not_empty_map.point((x,y,),fill=(elevation, elevation, elevation))
            x += 1
        y += 1 
    empty_map.show()


# blank_map = Image.new('RGBA', (600, 600), 'white')
# blank_map.save('test_map.png')
# draw_test = ImageDraw.Draw(blank_map)

#y, then x 
#return self.map_data_as_int[y][x]
#to get intensiy for each elevation, subtract minimum elevation from current elevation, divide that by the range, and you've got it!

# class ElevationMap:
#     """
#     ElevationMap is a class that takes a matrix (list of lists, 2D)
#     of integers and can be used to generate an image of those map_data_as_int
#     like a standard elevation map.
#     """

#     def __init__(self, map_data_as_int):
#         self.map_data_as_int = map_data_as_int

#     def elevation_at_coordinate(self, x, y):
#         return self.map_data_as_int[y][x]

#     def min_elevation(self):
#         return min([min(row) for row in self.map_data_as_int])

#     def max_elevation(self):
#         return max([max(row) for row in self.map_data_as_int])

#     def intensity_at_coordinate(self, x, y):
#         """Given an x, y coordinate, return the
#         intensity level (used for grayscale in image) of
#         the elevation at that coordinate.
#         """
#         elevation = self.elevation_at_coordinate(x, y)
#         min_elevation = self.min_elevation()
#         max_elevation = self.max_elevation()

#         return (elevation - min_elevation) / (max_elevation - min_elevation)


if __name__ == "__main__":
    #print(type(map_data_as_int_list[0]))
    #highest_elevation = max_of_data(map_data_as_int_list)
    #print(range_elevation)
    middle_moan = list_of_lists(cheap_sunglasses_indoors)
    #print(len(middle_moan[0]))
    # draw_map_from_ints(middle_moan)
    # print(middle_moan)
    # print(min_of_map_data)
    # print(range_of_map_data)
