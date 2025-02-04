#!/usr/bin/python3

def canUnlockAll(boxes):

    ret = []
    box = []

    for x in range(len(boxes)):
        box.append(x)
    
    print(box)

    for sublist in boxes:
        for key in sublist:
        

        
        


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))