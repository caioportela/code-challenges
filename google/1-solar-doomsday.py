import math

def solution(area):
    panels = []

    while area >= 1:
        panel_size = int(math.sqrt(area)) ** 2
        panels.append(panel_size)
        area -= panel_size

    return panels

if __name__ == '__main__':
    area = 15324
    result = solution(area)
    print(result)
