from collections import Counter
input = open("day5TestInput.txt", "r")



def parseData(): 

    allCords = []
    for line in input:
        cords = line.split(' -> ')
        startCords = cords[0].split(',')
        endCords = cords[1].replace("\n","").split(',')
        #print(startCords,endCords)

        if( startCords[0] == endCords[0] and startCords[1] != endCords[1]):
            high = max(int(startCords[1]),int(endCords[1]))
            low = min(int(startCords[1]),int(endCords[1]))
            print('a',startCords,endCords)

            for i in range(low,high+1):
                print(startCords[0]+','+str(i))
                allCords.append(startCords[0]+','+str(i))
        elif startCords[1] == endCords[1] and startCords[0] != endCords[0]:
            high = max(int(startCords[0]),int(endCords[0]))
            low = min(int(startCords[0]),int(endCords[0]))
            print('b',startCords,endCords)
            for i in range(low,high+1):
                print(str(i)+','+startCords[1])
                allCords.append(str(i)+','+startCords[1])
        
        elif(startCords[0] == endCords[1]):
            maxY = max(int(startCords[1]),int(startCords[0]))
            minX = min(int(startCords[1]),int(startCords[0]))
            index = maxY - minX

            for i in range(index+1):
                #print(str(minX+i)+','+str(maxY-i))
                allCords.append(str(minX+i)+','+str(maxY-i))
        elif(startCords[1] == startCords[0] and endCords[1] == endCords[0]):
            maxY = max(int(startCords[1]),int(endCords[0]))
            minX = min(int(startCords[1]),int(endCords[0]))
            for i in range(minX,maxY+1):
                #print(str(minX+i)+','+str(minX+i))
                allCords.append(str(minX+i)+','+str(minX+i))



    counter = Counter(allCords)
    dangerousZonesCount = 0
    for ele in counter:
        if counter[ele] > 1:
            dangerousZonesCount += 1
    #print(counter)
    print(dangerousZonesCount)

parseData()

input.close()