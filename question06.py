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


def rotate_image(img_arr):
    rotated = [[] for _ in range(len(img_arr))]
    count = 0

    for i, data in enumerate(img_arr):
        for j in range(0, len(data)):
            rotated[count].insert(j, img_arr[j][count])
        count += 1

    for i in range(0, len(rotated)):
        rotated[i] = list(reversed(rotated[i]))

    return rotated


print(rotate_image(a))

