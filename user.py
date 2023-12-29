currentPoint = startingPoint()
direction = ["Up", "Right", "Down", "Left"]

index = 3
while currentPoint != endPoint():
    index -= 1
    print(direction[index % 4])
    while seek(0, direction[index % 4]) == 1:
        index += 1

    print(direction[index % 4])
    move(0, direction[index % 4])
