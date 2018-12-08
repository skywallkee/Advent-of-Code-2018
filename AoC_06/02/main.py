def run(file_name):
    manhattan_limit=10000
    lines = [line.strip() for line in open(file_name, "r").readlines()]
    coords = set()
    maxLines = 0
    maxColumns = 0

    for line in lines:
        Line, Column = map(int, line.split(", "))
        coords.add((Line, Column))
        maxLines = max(maxLines, Line)
        maxColumns = max(maxColumns, Column)

    size_shared_region = 0

    for gridLine in range(maxLines + 1):
        for gridColumn in range(maxColumns + 1):
            size_shared_region += int(sum(abs(line - gridLine) + abs(column - gridColumn) for line, column in coords) < manhattan_limit)

    print(size_shared_region)


if __name__ == "__main__":
    file_name = "input_data.txt"
    run(file_name)
