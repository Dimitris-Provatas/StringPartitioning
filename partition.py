import math

def main():
    r = input("Type in a string: ")
    pos = []
    sets = []
    letterSets = []

    # print(len(r))
    for i in range(0, len(r)):
        for j in  range(len(r) - 1, i - 1, -1):
            # print(i, j)
            if (i <= j):
                if (r[i] == r[j]):
                    pos.append([i, j])
                    break
    pos.append([math.inf, math.inf])

    i = 0
    myMin = 0
    myMax = 0

    while (i >= myMin) and (i < len(pos) - 1):
        string = ""
        if (myMax >= pos[i + 1][0]):
            myMax = max(myMax, pos[i + 1][1])
            i += 1
        else:
            myMax = pos[i][1]
            sets.append([myMin, myMax])
            for j in range(myMin, myMax + 1):
                string += r[j]
            myMin = myMax + 1
            i = myMin
            letterSets.append(string)

    print("Partitioned string is: " + str(letterSets))

if (__name__) == "__main__":
    main()