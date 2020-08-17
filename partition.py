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
    myMax = pos[0][1]

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
    repeat()

def repeat():
    newInput = input("Input a new string? (Yes/No): ")

    if (newInput == "yes" or newInput == "y" or newInput == "YES" or newInput == "Y"):
        main()
    elif (newInput == "no" or newInput == "n" or newInput == "NO" or newInput == "N"):
        print("Exiting...")
        exit()
    else:
        print("No valid answer!")
        repeat()

if (__name__) == "__main__":
    main()