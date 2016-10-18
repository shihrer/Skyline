def addToSkyline(dimension):
    result = []
    result.append((dimension[0], 0))
    result.append((dimension[0], dimension[2]))
    result.append((dimension[1], dimension[2]))
    result.append((dimension[1], 0))
    return result


def mergeSkylines(one, two):
    result = []
    i = 0
    j = 0
    h1 = 0
    h2 = 0

    while i < len(one) and j < len(two):
        if one[i][0] < two[j][0]:
            h1 = one[i][1]
            result.append((one[i][0], max(h1,h2)))
            i += 1
        else:
            h2 = two[j][1]
            result.append((two[j][0], max(h1,h2)))
            j += 1
    while i < len(one):
        result.append(one[i])
        i += 1
    while j < len(two):
        result.append(two[j])
        j += 1

    return result


def skyline(input):
    if len(input) < 2:
        return addToSkyline(input[0])

    one = skyline(input[:len(input) // 2])
    two = skyline(input[len(input) // 2:])
    return mergeSkylines(one, two)


input1 = [(1, 3, 1), (2, 4, 2)]
input2 = [(1, 2, 2), (3, 4, 1)]
input3 = [(1,2,1), (2,5,2), (4,6,1)]
input4 = [(1,3,2), (2,4,1)]

print(skyline(input1))
print(skyline(input2))
print(skyline(input3))
print(skyline(input4))