"""
Sort any unsorted list given

"""


def sort_data(data):
    min_data = 0
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j+1] < data[j]:
                min_data = data[j+1]
                data[j+1] = data[j]
                data[j] = min_data
    return data


x = [15, 1, 9, 60, 1, 10, 8]
print(sort_data(x))
