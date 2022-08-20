import sys

def tower_game(n, events):
    x_heights = {}
    max_height = 0
    gold_height = []
    points = 0
    ret = []
    for i in events:
        x_heights.update({str(i[0]): 0})
    for i in events:
        if i[1] == 1: #gold block
            x_heights[str(i[0])] += 1
            max_value = max(x_heights, key=x_heights.get)
            if (x_heights[str(max_value)] == x_heights[str(i[0])]) and (x_heights[str(i[0])] > max_height):
                points += 1
                max_height = x_heights[str(i[0])]
            if x_heights[str(i[0])] not in gold_height:
                points += 1
                gold_height.append(x_heights[str(i[0])])
            ret.append(points)
        elif i[1] == 2 or i[1] == 3: #horizontal blocks
            if i[1] == 2:
                positions = [int(i[0]), int(i[0]) + 1]
            elif i[1] == 3:
                positions = [int(i[0]), int(i[0]) + 1, int(i[0]) + 2]
            peak = 0
            for x in positions:
                if str(x) not in x_heights.keys():
                    x_heights.update({str(x): 0})
            for each in positions:
                if x_heights[str(each)] > peak:
                    peak = x_heights[str(each)]
            for x in positions:
                x_heights[str(x)] = peak + 1
            max_value = max(x_heights, key=x_heights.get)
            if (x_heights[str(i[0])] == x_heights[str(max_value)]) and (x_heights[str(i[0])] > max_height):
                points += 1
                max_height = x_heights[str(i[0])]
            ret.append(points)
        elif i[1] >= 4: #long vertical blocks
            x_heights[str(i[0])] += i[1]
            max_value = max(x_heights, key=x_heights.get)
            if (x_heights[str(max_value)] == x_heights[str(i[0])]) and (x_heights[str(i[0])] > max_height):
                points += 1
                max_height = x_heights[str(i[0])]
            ret.append(points)
    return ret


# Reads the input
astr = reader.readline().split()
n = int(astr[0])
events = [[int(val) for val in reader.readline().split()] for _ in range(0,n)]

# Calls your function
ret = tower_game(n, events)

# Writes the output
for i in range(0,n):
    print(ret[i])
