def generate(numRows: int):
    triangle =[]
    for i in range(numRows):
        if i == 0:
            triangle.append([1])
            continue

        prev = [0] + triangle[i-1] + [0]

        row = []
        for i in range(1, len(prev)):
            row.append(prev[i] + prev[i-1])

        triangle.append(row)
    return triangle

print(generate(3))