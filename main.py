import csv
with open('input.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    nr = int(input("Numarul de productii este: "))
    numCuv = int(input("Numarul de cuvinte date: "))

    productionsContainer = [[0] * 10 for i in range(nr)]
    i = 0  # numarul liniei curente din fisierul de citire
    j = 0  # index numar productii
    finalStatesList = []
    wordsList = []
    indexCuv = 0

    for line in csv_reader:
        i = i + 1
        if i <= numCuv:
            wordsList.append(line)
        elif i == numCuv+1:
            statesList = line
        elif i == numCuv + 2:
            T = line
        elif i > numCuv + 2:
            if line[1] == '#':
                finalStatesList.append(line[0])
            productionsContainer[j] = line
            j = j + 1

    crtState = statesList[0]
    i = 0

    for word in wordsList:
        crtState = statesList[0]  # starea curenta a automatului

        for i in range(len(word)):
            ok = 0
            if word[i] not in T:
                print("NU apartine limbajului")
                break
            else:
                ok = 0
                if i == len(word) - 1:

                    for line in productionsContainer:
                        if line[1] == word[i] and line[2] in finalStatesList and line[0] == crtState:
                            print("Apartine limbajului")
                            ok = 1
                            break
                    if ok == 0:
                        print("Nu apartine")
                    break
                else:

                    for line in productionsContainer:
                        if line[1] == word[i] and line[0] == crtState:
                            ok = 1
                            crtState = line[2]
                            break
                    if ok == 0:
                        print("NU apartine")
                        break

