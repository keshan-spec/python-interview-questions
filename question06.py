"""
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


# :arg - array
# :return - a new array of the rotated images
def rotate_image(img_arr):
    # copy the shape of the provided array
    rotated = [[] for _ in range(len(img_arr))]
    count = 0

    # loop over the image array
    for i, data in enumerate(img_arr):
        for j in range(0, len(data)):
            # append the vertical values of the inner arrays
            # example : [[x,y],[a,b]] -> [[x,a],[y,b]]
            rotated[count].insert(j, img_arr[j][count])
        count += 1

    # loop over the new list and reverse them to rotate 90 deg
    # example : [[x,a],[y,b]] -> [[a,x],[b,y]]
    for i in range(0, len(rotated)):
        rotated[i] = list(reversed(rotated[i]))

    # return the rotated image array
    return rotated


print(rotate_image(a))
