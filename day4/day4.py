input = open("day4Input.txt", "r")


def parseData():
    bingoNumbers = []
    bingoCards = []
    i = -1
    arr = []
    for line in input:
        #print(line)
        if line == "\n":
            i += 1
            if(i > 0):
                bingoCards.append(arr)
                arr = []
            continue
        if i == -1:
            bingoNumbers = bingoNumbers + line.replace("\n", " ").split(",")
        else:
            k = line.replace("\n","").split(" ")
            k = list(filter(lambda x : x != "", k))
            arr.append(k)
    bingoCards.append(arr)
    return bingoNumbers, bingoCards

def checkForBingo(bingoCard):
    for row in bingoCard:
        if(len(list(filter(lambda x : x == -1, row))) == 5):
            return True
    else:
        for i in range(0,5):
            for j in range(0,5):
                if bingoCard[j][i] == -1:
                    if j == 4: 
                        return True
                    continue;
                else:
                    break
    return False

def completeBingo(bingoNumbers,bingoCards):
    for bingoNumber in bingoNumbers:
        for bingoCard in bingoCards:
            for row in bingoCard:
                try:
                    row[row.index(bingoNumber)] = -1
                    break
                except:
                    continue
        for bingoCard in bingoCards:
            if checkForBingo(bingoCard):
                return bingoNumber,bingoCard

def completeLosingBingo(bingoNumbers,bingoCards):
    number = 0
    for bingoNumber in bingoNumbers:
        for bingoCard in bingoCards:
            for row in bingoCard:
                try:
                    row[row.index(bingoNumber)] = -1
                    break
                except:
                    continue
        for bingoCard in bingoCards:
            if checkForBingo(bingoCard):
                bingoCards.remove(bingoCard)
        if(len(bingoCards) == 0):
            return bingoNumber,bingoCard

def computeSum(bingoCard,lastNumber):
    unmarkedSum = 0
    for row in bingoCard:
        for n in row:
            if n != -1:
                unmarkedSum += int(n)
    return unmarkedSum * int(lastNumber)


def day4Part1():
    bingoNumbers,bingoCards = parseData()    
    lastNumber, winningCard = completeBingo(bingoNumbers,bingoCards)
    print(computeSum(winningCard,lastNumber))

def day4Part2():
    bingoNumbers,bingoCards = parseData()    
    lastNumber, losingCard = completeLosingBingo(bingoNumbers,bingoCards)
    print(computeSum(losingCard,lastNumber))

day4Part2()