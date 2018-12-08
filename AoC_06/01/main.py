from collections import defaultdict

def getCoordinates(lines):
    coordinates = set()
    maxLine = 0
    maxColumn = 0
    
    for line in lines:
        line, column = map(int, line.split(", "))
        coordinates.add((line, column))
        maxLine = max(maxLine, line)
        maxColumn = max(maxColumn, column)
    return coordinates, maxLine, maxColumn

def getRegions(coordinates, maxLine, maxColumn):
    coord_id_to_point = {coordId: point for coordId, point in enumerate(coordinates, start=1)}
    regionSizes = defaultdict(int)
    infiniteIds = set()
    for i in range(maxLine + 1):
        for j in range(maxColumn + 1):
            min_dists = sorted([(abs(r - i) + abs(c - j), coordId) for coordId, (r, c) in coord_id_to_point.items()])

            if len(min_dists) == 1 or min_dists[0][0] != min_dists[1][0]:
                coordId = min_dists[0][1]
                regionSizes[coordId] += 1

                if i == 0 or i == maxLine or j == 0 or j == maxColumn:
                    infiniteIds.add(coordId)
                    
    return regionSizes, infiniteIds

def run(file_name):

    lines = [line.strip() for line in open(file_name, "r").readlines()]
    coordinates, maxLine, maxColumn = getCoordinates(lines)
    regionSizes, infiniteIds = getRegions(coordinates, maxLine, maxColumn)
    print(max(size for coordId, size in regionSizes.items() if coordId not in infiniteIds))

if __name__ == "__main__":
    file_name = "input_data.txt"
    run(file_name)
