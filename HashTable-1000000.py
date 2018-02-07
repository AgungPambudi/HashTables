import math
import random
import time

def newHashTable(size):
    hashTable = [None] * size
    return hashTable

def getMiddle(aNumber):
    numString = str(aNumber)
    midPoint = len(numString) // 2
    if (len(numString) % 2) == 0:
        middle = int(numString[midPoint - 1:midPoint + 1])
    else:
        middle = int(numString[midPoint])
    return middle

def getHashSlot(aNumber, size):
    aNumber ** 2
    mid = getMiddle(aNumber)
    return mid % size

def hashSize(size):
    size *= 2
    if size % 2 == 0:
        return size + 1
    if size % 3 == 0:
        return size + 1
    return size

def createHashTable(integers):
    start = time.time()
    size = len(integers)
    hashTable = newHashTable(hashSize(size))
    print("\nHash Table Size: ", len(hashTable))
    print("Entries: ", len(integers))
    j = 0
    for i in integers:
        slot = getHashSlot(i, len(hashTable))
        done = False
        while not done:
            if hashTable[slot] != None:
                j += 1
                # print("="*20)
                # print(hashTable)
                # print(i)
                # print("slot ", slot, " occupied")
                slot = (slot + (j * j)) % len(hashTable)
                # print("new slot ", slot)
            else:
                hashTable[slot] = i
                done = True
    end = time.time()
    print(end - start, "\n")
    return hashTable

listSize = random.randint(0, 10000)

ints = []
for i in range(0, 1000000):
    ints.append(random.randint(0, 1000000))

createHashTable(ints)

