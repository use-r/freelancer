
import matplotlib.pyplot as plt
from queue import Queue


def iswhite(value):
    if value == 1:
        return True


def getadjacent(n):
    x, y = n
    return [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]


def BFS(start, end, pixels):
    queue = Queue()
    queue.put([start])

    while not queue.empty():

        path = queue.get()
        pixel = path[-1]

        if pixel == end:
            return path

        for adjacent in getadjacent(pixel):
            x, y = adjacent

            if x < 0 or y < 0 or x > 100 or y > 100:
                continue

            print(x, y)
            if iswhite(pixels[x, y]):
                pixels[x, y] = 0.5
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)

    print("Queue has been exhausted. No answer was found.")


if __name__ == '__main__':
    base_pixels = plt.imread('maze.png')
    path_pixels = base_pixels.copy()
    start = (1, 0)  # start coordicate
    end = (99, 100)  # goal coordinate
    path = BFS(start, end, base_pixels)

    for position in path:
        x, y = position
        path_pixels[x, y] = 0.5

    plt.figure()
    plt.imshow(path_pixels, cmap='gray')
    plt.axis('off')
    plt.savefig('maze_solved.png')
    plt.show()
