import time


def Bubble_sort(data, Draw):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j + 1] < data[j]:
                data[j + 1], data[j] = data[j], data[j + 1]
                Draw(data, ['red' if x == j or x == j + 1 else 'black' for x in range(len(data))])
                time.sleep(0.45)
    Draw(data, ['green' for x in range(len(data))])
