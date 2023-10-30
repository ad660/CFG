purple_heights = [5, 8, 1, 3, 4]
black_heights = [6, 9, 2, 4, 5]

row1 = input("Please add heights separated by commas")
row2 = input("Please add second row of heights separated by commas")

row1.split()
row2.split()
def createList(row):
    for i in range(len(row)):
        row[i] = int(row[i])
        print(row)


createList(row1)

purple_heights.sort()
black_heights.sort()

print(purple_heights, black_heights)


def checkHeights(row1 , row2):
    row1.list