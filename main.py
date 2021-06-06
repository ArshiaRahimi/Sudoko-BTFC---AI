import numpy as np
import copy
"""
Format of Input:

m(number of colors)     n(dimensions of the table)

r g b y p ... (for i=0 to m) priority is considered from left to right

1#   *b   *#
*#   3r   *#
*g   1#   *#
"""

# priority = ['r', 'g', 'b', 'y', 'p']


def colorPriority(c1, c2):
    index1 = priority.index(c1)
    index2 = priority.index(c2)
    if index1 > index2:
        return c2
    if index1 < index2:
        return c1


# color1 is the higher number
def checkPriority(colorOne, colorTwo):
    index1 = priority.index(colorOne)
    index2 = priority.index(colorTwo)
    if index1 > index2:
        # color 1 have the higher priority
        return False


def checkPriority2(colorOne, colorTwo):
    if colorOne != "#" and colorTwo != "#":
        index1 = priority.index(colorOne)
        index2 = priority.index(colorTwo)
        # print("index 1 : " + str(index1))
        # print("index 2: "+ str(index2))
        if index1 > index2:
            return False



#print(checkPriority('b','g'))

"""
   |  -         (i-1, j)      -     |
   | (i, j-1)   (i, j)      (i, j+1)|
   |  -         (i+1, j)      -     |
"""

color1 = [['#', 'z', 'p'],
         ['u', '#', 'r'],
         ['#', 'x', '#']]

color2 = [['y', 'b', 'g'],
         ['b', 'y', 'p'],
         ['g', 'r', 'g']]

#print(checkPriority(color2[1][1], color2[2][1]))
# (1,0) (1,1) (1,2)


def checkColor(array2d, n):
    for i in range(n):
        for j in range(n):
            # print("i:"+str(i)+" j:"+str(j))
            if i-1 in range(n):
                if array2d[i][j] != '#':
                    if array2d[i][j] == array2d[i - 1][j]:
                        return False
                else:
                    return False
            if j-1 in range(n):
                if array2d[i][j] != '#':
                    if array2d[i][j] == array2d[i][j - 1]:
                        return False
                else:
                    return False
            if j+1 in range(n):
                if array2d[i][j] != '#':
                    if array2d[i][j] == array2d[i][j + 1]:
                        return False
                else:
                    return False
            if i+1 in range(n):
                if array2d[i][j] != '#':
                    if array2d[i][j] == array2d[i + 1][j]:
                        return False
                else:
                    return False

    return True

# print(checkColor(color2, 3))


def checkNumber(array2d, n):
    for row in array2d:
        validNumbers = [str(i + 1) for i in range(n)]
        for index in row:
            if index not in validNumbers:
                return False
            else:
                validNumbers.remove(index)
    k = 0
    while k != n:
        validNumbers = [str(i + 1) for i in range(n)]
        for column in [str(row[k]) for row in array2d]:
            #  print(column)
            if column not in validNumbers:
                return False
            else:
                validNumbers.remove(column)
        # print("\n")
        k += 1

    return True


def goalTest(node, n):
    Numbers = []
    Colors = []
    for row in node:
        newRow = []
        newRow2 = []
        for element in row:
            newRow.append(element[0])
            newRow2.append(element[1])
        Numbers.append(newRow)
        Colors.append(newRow2)
    # checkNumber(Numbers, n)
    # checkColor(Colors, n)
    for i in range(n):
        for j in range(n):
            if i-1 in range(n):
                if checkColor(Colors, n) is True and checkNumber(Numbers, n) is True:
                    if Numbers[i][j] < Numbers[i - 1][j]:
                        if checkPriority(Colors[i - 1][j], Colors[i][j]) is False:
                            return False
                    else:
                        if checkPriority(Colors[i][j], Colors[i - 1][j]) is False:
                            return False
                else:
                    return False
            if j-1 in range(n):
                if checkColor(Colors, n) is True and checkNumber(Numbers, n) is True:
                    if Numbers[i][j] < Numbers[i][j - 1]:
                        if checkPriority(Colors[i][j - 1], Colors[i][j]) is False:
                            return False
                    else:
                        if checkPriority(Colors[i][j], Colors[i][j - 1]) is False:
                            return False
                else:
                    return False
            if j+1 in range(n):
                if checkColor(Colors, n) is True and checkNumber(Numbers, n) is True:
                    if Numbers[i][j] < Numbers[i][j + 1]:
                        if checkPriority(Colors[i][j + 1], Colors[i][j]) is False:
                            return False
                    else:
                        if checkPriority(Colors[i][j], Colors[i][j + 1]) is False:
                            return False
                else:
                    return False
            if i+1 in range(n):
                if checkColor(Colors, n) is True and checkNumber(Numbers, n) is True:
                    if Numbers[i][j] < Numbers[i + 1][j]:
                        if checkPriority(Colors[i + 1][j], Colors[i][j]) is False:
                            return False
                    else:
                        if checkPriority(Colors[i][j], Colors[i + 1][j]) is False:
                            return False
                else:
                    return False
    return True


test1 = [['1#', '*b', '*#'],
         ['*#', '3r', '*#'],
         ['*g', '1#', '*#']]


def makeDomain(node, n):
    domain = []
    tag = 1
    for row in node:
        for element in row:
            # [i+1 for i in range(n)]
            newElement = [tag, element[0], element[1]]
            if element[0] == '*':
                newElement[1] = [i+1 for i in range(n)]
            if element[1] == '#':
                newElement[2] = [j for j in priority]
            tag += 1
            domain.append(newElement)
    return domain

completeTest = [['1y', '2b', '3g'],
              ['2b', '3r', '1p'],
              ['3g', '1y', '2g']]

def MRV(node):
    chooseFrom = []
    lenArray = []
    candidateArray = []
    for i in node:
        for j in i:
            if isinstance(j, str) or isinstance(j, int):
                continue
            choose = [i[0], j, len(j)]
            lenArray.append(len(j))
            chooseFrom.append(choose)
    lowestAmount = min(lenArray)
    for element in chooseFrom:
        if element[2] == lowestAmount:
            candidateArray.append(element)
    idx = np.random.randint(len(candidateArray), size=1)
    return candidateArray[int(idx)]


def mapNumToAddress(n, cordinate):
    findYa = 1
    for row in range(n):
        for element in range(n):
            if findYa == cordinate:
                return row, element
            findYa += 1

# print(mapNumToAddress(3, 9))


def DEGREE(node, n):
    chooseFrom = []
    lenArray = []
    candidateArray = []
    for i in node:
        numberDegree = 1
        colorDegree = 1
        x, y = mapNumToAddress(n, i[0])
        for j in node:
            xxx, yyy = mapNumToAddress(n, j[0])
            if x == xxx and y != yyy:
                if isinstance(j[1], str) is False:
                    numberDegree += 1
            if y == yyy and x != xxx:
                if isinstance(j[1], str) is False:
                    numberDegree += 1
            if x-1 == xxx and y == yyy:
                if isinstance(j[2], str) is False:
                    colorDegree += 1
            if x == xxx and y-1 == yyy:
                if isinstance(j[2], str) is False:
                    colorDegree += 1
            if x == xxx and y+1 == yyy:
                if isinstance(j[2], str) is False:
                    colorDegree += 1
            if x+1 == xxx and y == yyy:
                if isinstance(j[2], str) is False:
                    colorDegree += 1
        degree = colorDegree + numberDegree
        for k in i:
            if isinstance(k, str) or isinstance(k, int):
                continue
            choose = [i[0], k, degree]
            chooseFrom.append(choose)
            lenArray.append(degree)
    highestAmount = max(lenArray)
    for element in chooseFrom:
        if element[2] == highestAmount:
            candidateArray.append(element)
    idx = np.random.randint(len(candidateArray), size=1)
    return candidateArray[int(idx)]


def Degree2(node, n, candidate_array):
    chooseFrom = []
    lenArray = []
    candidateArray = []
    for i in candidate_array:
        numberDegree = 1
        colorDegree = 1
        x, y = mapNumToAddress(n, i[0])
        for j in node:
            xxx, yyy = mapNumToAddress(n, j[0])
            if x == xxx and y != yyy:
                if isinstance(j[1], str) is False:
                    numberDegree += 1
            if y == yyy and x != xxx:
                if isinstance(j[1], str) is False:
                    numberDegree += 1
            if x - 1 == xxx and y == yyy:
                if isinstance(j[2], str) is False:
                    colorDegree += 1
            if x == xxx and y - 1 == yyy:
                if isinstance(j[2], str) is False:
                    colorDegree += 1
            if x == xxx and y + 1 == yyy:
                if isinstance(j[2], str) is False:
                    colorDegree += 1
            if x + 1 == xxx and y == yyy:
                if isinstance(j[2], str) is False:
                    colorDegree += 1
        degree = colorDegree + numberDegree
        for k in i:
            if isinstance(k, str) or isinstance(k, int):
                continue
            choose = [i[0], k, degree]
            chooseFrom.append(choose)
            lenArray.append(degree)
    highestAmount = max(lenArray)
    for element in chooseFrom:
        if element[2] == highestAmount:
            candidateArray.append(element)
    idx = np.random.randint(len(candidateArray), size=1)
    return candidateArray[int(idx)]


def MRV_Degree(node, n):
    chooseFrom = []
    lenArray = []
    candidateArray = []
    for i in node:
        for j in i:
            if isinstance(j, str) or isinstance(j, int):
                continue
            choose = [i[0], j, len(j)]
            lenArray.append(len(j))
            chooseFrom.append(choose)
    lowestAmount = min(lenArray)
    for element in chooseFrom:
        if element[2] == lowestAmount:
            candidateArray.append(element)
    # print(candidateArray)
    if len(candidateArray) == 1:
        return candidateArray[0]
    else:
        return Degree2(node, n, candidateArray)


test2 = [['*#', '2b', '3g'],
         ['2b', '*r', '1p'],
         ['3#', '1y', '2#']]

# print(MRV_Degree(makeDomain(test2, 3), 3))


replaceTest = [['1#', '*b', '*#'],
              ['*#', '3r', '*#'],
              ['*g', '1#', '*#']]


def checkColor2(array2d, n):
    for i in range(n):
        for j in range(n):
            # print("i:"+str(i)+" j:"+str(j))
            if i-1 in range(n):
                if array2d[i][j] != '#':
                    if array2d[i][j] == array2d[i - 1][j]:
                        return False
            if j-1 in range(n):
                if array2d[i][j] != '#':
                    if array2d[i][j] == array2d[i][j - 1]:
                        return False
            if j+1 in range(n):
                if array2d[i][j] != '#':
                    if array2d[i][j] == array2d[i][j + 1]:
                        return False
            if i+1 in range(n):
                if array2d[i][j] != '#':
                    if array2d[i][j] == array2d[i + 1][j]:
                        return False

    return True


def checkNumber2(array2d, n):
    for row in array2d:
        validNumbers = [str(i + 1) for i in range(n)]
        for index in row:
            if index == "*":
                continue
            if index not in validNumbers:
                return False
            else:
                validNumbers.remove(index)
    k = 0
    while k != n:
        validNumbers = [str(i + 1) for i in range(n)]
        for column in [str(row[k]) for row in array2d]:
            #  print(column)
            if column == "*":
                continue
            if column not in validNumbers:
                return False
            else:
                validNumbers.remove(column)
        # print("\n")
        k += 1
    return True


def checkConsistency(node, n):
    Numbers = []
    Colors = []
    for row in node:
        newRow = []
        newRow2 = []
        for element in row:
            newRow.append(element[0])
            newRow2.append(element[1])
        Numbers.append(newRow)
        Colors.append(newRow2)
    # checkNumber(Numbers, n)
    # checkColor(Colors, n)
    for i in range(n):
        for j in range(n):
            if i-1 in range(n):
                if checkColor2(Colors, n) is True and checkNumber2(Numbers, n) is True:
                    if Numbers[i][j] != "*" and Numbers[i-1][j] != "*":
                        if Numbers[i][j] < Numbers[i - 1][j]:
                            if checkPriority2(Colors[i - 1][j], Colors[i][j]) is False:
                                return False
                        else:
                            if checkPriority2(Colors[i][j], Colors[i - 1][j]) is False:
                                return False
                else:
                    return False
            if j-1 in range(n):
                if checkColor2(Colors, n) is True and checkNumber2(Numbers, n) is True:
                    if Numbers[i][j] != "*" and Numbers[i][j - 1] != "*":
                        if Numbers[i][j] < Numbers[i][j - 1]:
                            if checkPriority2(Colors[i][j - 1], Colors[i][j]) is False:
                                return False
                        else:
                            if checkPriority2(Colors[i][j], Colors[i][j - 1]) is False:
                                return False
                else:
                    return False
            if j+1 in range(n):
                if checkColor2(Colors, n) is True and checkNumber2(Numbers, n) is True:
                    if Numbers[i][j] != "*" and Numbers[i][j + 1] != "*":
                        if Numbers[i][j] < Numbers[i][j + 1]:
                            if checkPriority2(Colors[i][j + 1], Colors[i][j]) is False:
                                return False
                        else:
                            if checkPriority2(Colors[i][j], Colors[i][j + 1]) is False:
                                return False
                else:
                    return False
            if i+1 in range(n):
                if checkColor2(Colors, n) is True and checkNumber2(Numbers, n) is True:
                    if Numbers[i][j] != "*" and Numbers[i+1][j] != "*":
                        if Numbers[i][j] < Numbers[i + 1][j]:
                            if checkPriority2(Colors[i + 1][j], Colors[i][j]) is False:
                                return False
                        else:
                            if checkPriority2(Colors[i][j], Colors[i + 1][j]) is False:
                                # print("i, j : " +str(Numbers[i][j]))
                                # print("i+1, j :" + str(Numbers[i+1][j]))
                                return False
                else:
                    return False
    return True

aa = [['1r', '*b', '*#'],
     ['*#', '3r', '*#'],
    ['*g', '1#', '*#']]
test3 = [['3r', '2b', '*#'],
         ['*#', '*#', '*#'],
         ['*#', '*#', '*#']]
# print(checkConsistency(aa, 3))

# format of domain is [[1,'1',['r', 'g', 'b']], [2, ['1', '2', '3'], ['r', 'g', 'b']], ...]
"""
   |  -         (i-1, j)      -     |
   | (i, j-1)   (i, j)      (i, j+1)|
   |  -         (i+1, j)      -     |
"""

# (i, j) => coordinate


def mapIJToCoordinate(i, j, n):
    num = 1
    for rw in range(n):
        for cl in range(n):
            if rw == i and cl == j:
                return num
            num += 1


def removeFromDomain(domain, coordinate, n):
    x_of_main, y_of_main = mapNumToAddress(n, coordinate)
    # remove domains from (left, right, up, down) of (x_of_main, y_of_main)
    for row in domain:
        if row[0] == coordinate:
            number = row[1]
            color = row[2]

    if len(color) == 1 and isinstance(color, list) is False:
        for ii in domain:
            if mapIJToCoordinate(x_of_main - 1, y_of_main, n) == ii[0]:
                if color in ii[2]:
                    ii[2].remove(color)
            if mapIJToCoordinate(x_of_main, y_of_main - 1, n) == ii[0]:
                if color in ii[2]:
                    ii[2].remove(color)
            if mapIJToCoordinate(x_of_main, y_of_main + 1, n) == ii[0]:
                if color in ii[2]:
                    ii[2].remove(color)
            if mapIJToCoordinate(x_of_main + 1, y_of_main, n) == ii[0]:
                if color in ii[2]:
                    ii[2].remove(color)
    if len(number) == 1 and isinstance(number, list) is False:
        for jj in domain:
            xxx, yyy = mapNumToAddress(n, jj[0])
            if isinstance(jj[1], str):
                continue
            if x_of_main == xxx and y_of_main != yyy:
                if int(number) in jj[1]:
                    index = jj[1].index(int(number))
                    jj[1].pop(index)
            if y_of_main == yyy and x_of_main != xxx:
                # print("cor "+ str(coordinate) + "num "+str(number))
                #print("")
                if int(number) in jj[1]:
                    index = jj[1].index(int(number))
                    jj[1].pop(index)
    if len(number) == 1 and len(color) == 1 and isinstance(number, list) is False and isinstance(color, list) is False:
        for kk in domain:

            if mapIJToCoordinate(x_of_main - 1, y_of_main, n) == kk[0]:
                if isinstance(kk[1], str) is True and isinstance(kk[2], str) is False:
                    if int(number) > int(kk[1]):
                        temp = []
                        for v in kk[2]:
                            if colorPriority(color, v) == v:
                                temp.append(v)
                        for tmp in temp:
                            kk[2].remove(tmp)

                    if int(number) < int(kk[1]):
                        temp = []
                        for v in kk[2]:
                            if colorPriority(color, v) == color:
                                temp.append(v)
                        for tmp in temp:
                            kk[2].remove(tmp)

                if isinstance(kk[2], str) is True and isinstance(kk[1], str) is False:
                    if colorPriority(color, kk[2]) == color:
                        temp = []
                        for v in kk[1]:
                            if v > int(number):
                                temp.append(v)
                        for tmp in temp:
                            kk[1].remove(tmp)
                    if colorPriority(color, kk[2]) == kk[2]:
                        temp = []
                        for v in kk[1]:
                            if v < int(number):
                                temp.append(v)
                        for tmp in temp:
                            kk[1].remove(tmp)

            if mapIJToCoordinate(x_of_main, y_of_main - 1, n) == kk[0]:
                if isinstance(kk[1], str) is True and isinstance(kk[2], str) is False:
                    if int(number) > int(kk[1]):
                        temp = []
                        for v in kk[2]:
                            if colorPriority(color, v) == v:
                                temp.append(v)
                        for tmp in temp:
                            kk[2].remove(tmp)

                    if int(number) < int(kk[1]):
                        temp = []
                        for v in kk[2]:
                            if colorPriority(color, v) == color:
                                temp.append(v)
                        for tmp in temp:
                            kk[2].remove(tmp)

                if isinstance(kk[2], str) is True and isinstance(kk[1], str) is False:
                    if colorPriority(color, kk[2]) == color:
                        temp = []
                        for v in kk[1]:
                            if v > int(number):
                                temp.append(v)
                        for tmp in temp:
                            kk[1].remove(tmp)
                    if colorPriority(color, kk[2]) == kk[2]:
                        temp = []
                        for v in kk[1]:
                            if v < int(number):
                                temp.append(v)
                        for tmp in temp:
                            kk[1].remove(tmp)

            if mapIJToCoordinate(x_of_main, y_of_main + 1, n) == kk[0]:
                if isinstance(kk[1], str) is True and isinstance(kk[2], str) is False:
                    if int(number) > int(kk[1]):
                        temp = []
                        for v in kk[2]:
                            if colorPriority(color, v) == v:
                                temp.append(v)
                        for tmp in temp:
                            kk[2].remove(tmp)

                    if int(number) < int(kk[1]):
                        temp = []
                        for v in kk[2]:
                            if colorPriority(color, v) == color:
                                temp.append(v)
                        for tmp in temp:
                            kk[2].remove(tmp)

                if isinstance(kk[2], str) is True and isinstance(kk[1], str) is False:
                    if colorPriority(color, kk[2]) == color:
                        temp = []
                        for v in kk[1]:
                            if v > int(number):
                                temp.append(v)
                        for tmp in temp:
                            kk[1].remove(tmp)
                    if colorPriority(color, kk[2]) == kk[2]:
                        temp = []
                        for v in kk[1]:
                            if v < int(number):
                                temp.append(v)
                        for tmp in temp:
                            kk[1].remove(tmp)

            if mapIJToCoordinate(x_of_main + 1, y_of_main, n) == kk[0]:
                if isinstance(kk[1], str) is True and isinstance(kk[2], str) is False:
                    if int(number) > int(kk[1]):
                        temp = []
                        for v in kk[2]:
                            if colorPriority(color, v) == v:
                                temp.append(v)
                        for tmp in temp:
                            kk[2].remove(tmp)

                    if int(number) < int(kk[1]):
                        temp = []
                        for v in kk[2]:
                            if colorPriority(color, v) == color:
                                temp.append(v)
                        for tmp in temp:
                            kk[2].remove(tmp)

                if isinstance(kk[2], str) is True and isinstance(kk[1], str) is False:
                    if colorPriority(color, kk[2]) == color:
                        temp = []
                        for v in kk[1]:
                            if v > int(number):
                                temp.append(v)
                        for tmp in temp:
                            kk[1].remove(tmp)
                    if colorPriority(color, kk[2]) == kk[2]:
                        temp = []
                        for v in kk[1]:
                            if v < int(number):
                                temp.append(v)
                        for tmp in temp:
                            kk[1].remove(tmp)

    return domain


replaceTest2 = [['1#', '3#', '2#'],
              ['2#', '1#', '3#'],
              ['3#', '2#', '1#']]


def insertIntoNode(node, value, coordinate, n):
    # node = copy.deepcopy(node)
    if isinstance(value, int):
        x, y = mapNumToAddress(n, coordinate)
        new = list(node[x][y])
        index1 = new.index("*")
        new[index1] = str(value)
        str1 = ''.join(new)
        node[x][y] = str1
    if isinstance(value, str):
        x, y = mapNumToAddress(n, coordinate)
        new2 = list(node[x][y])
        index2 = new2.index("#")
        new2[index2] = value
        str2 = ''.join(new2)
        node[x][y] = str2
    return node


def removeFromNode(node, value, coordinate, nn):
    # node = copy.deepcopy(node)
    if isinstance(value, int):
        x, y = mapNumToAddress(nn, coordinate)
        new = list(node[x][y])
        # print(new)
        index1 = new.index(str(value))
        new[index1] = "*"
        str1 = ''.join(new)
        node[x][y] = str1
    if isinstance(value, str):
        x, y = mapNumToAddress(nn, coordinate)
        new = list(node[x][y])
        # print(new)
        index1 = new.index(value)
        new[index1] = "#"
        str1 = ''.join(new)
        node[x][y] = str1
    return node


def remove_all_domain(domain, n):
    for i in range(n*n):
        domain=removeFromDomain(domain, i+1, n)
    return domain



def BT_FC2(node, n, domain):
    print("running")
    if goalTest(node, n) is True:
        for i in node:
            print(i)
        return node
    # candidate = MRV(domain)
    candidate = MRV_Degree(domain, n)
    # candidate = DEGREE(domain, n)
    coordinate = candidate[0]
    for x in candidate[1]:
        inserted = insertIntoNode(node, x, coordinate, n)
        # print(inserted)
        domainWipeOut = False
        if checkConsistency(inserted, n) is True:
            # insertValueIntoNode(node, x, coordinate, n)
            # domainPrime = removeFromDomain(makeDomain(inserted, n), coordinate, n)
            domainPrime = remove_all_domain(makeDomain(inserted, n), n)
            print(domainPrime)
            for row in domainPrime:
                if not row[1] or not row[2]:
                    # print("hahaha")
                    domainWipeOut = True
                    break
            if not domainWipeOut:
                if BT_FC2(inserted, n, domainPrime):
                    return True
        removeFromNode(inserted, x, coordinate, n)


emptyTest = [['4#','*#','*#', '*#', '*#'],
            ['*g','*#','2#','1#', '*r'],
            ['*#','1y','*#','*#', '*#'],
            ['*y','*b','3#','*r', '*#'],
             ['2#','*#','*#','*g', '*#']]

"""for i in removeFromDomain(makeDomain(bigAssTest, 9), 1, 9):
    print(i)"""
# print(BT_FC2(test2, 3,makeDomain(test2, 3)))
# print(BT_FC2(replaceTest2, 3,remove_all_domain(makeDomain(replaceTest2, 3), 3)))
# print(BT_FC2(replaceTest, 3, remove_all_domain(makeDomain(replaceTest, 3), 3)))
# print(BT_FC2(emptyTest, 5,remove_all_domain(makeDomain(emptyTest, 5), 5)))

if __name__ == '__main__':
    user_input = input("Please enter m n ")
    splitter = user_input.split()
    priority = []
    startNode = []
    if len(splitter) > 2:
        print("You entered more than 3 variables!")
    else:
        m = int(splitter[0])
        n = int(splitter[1])
        priorityInput = input()
        priority = priorityInput.split()
        # print(priority)
        for j in range(n):
            row = input()
            rowSplitter = row.split()
            startNode.append(rowSplitter)
        # print(startNode)
        print(BT_FC2(startNode, n,remove_all_domain(makeDomain(startNode, n), n)))


