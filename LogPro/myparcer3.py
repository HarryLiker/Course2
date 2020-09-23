# -*- coding: utf-8 -*-

import re

# ^ - начало строки
# $ - конец строки
# \s - любой пробельный символ
# \d - любая цифра [0;9]
# () - группирует выражение и возвращает найденный текст
# . - один любой символ, кроме новой строки
# + - 1 и более вхождений шаблона слева
# * - 0 и более вхождений шаблона слева

def findID(line): 
    ID = re.search(r"^0\s+@I(\d+)@\s+INDI$", line)
    if ID is not None:
        return ID.group(1)

def findName(line):
    Name = re.search(r"^1\s+NAME\s+(.+)\s+/(.*)/$", line)
    if Name is not None:
        if Name.group(2) == "":
            return Name.group(1)
        else:
            return Name.group(1) + " " + Name.group(2)

if __name__ == '__main__':
    outfile = open("facts.pl", "w", encoding='utf8')

    fileLines = []
    with open("MyTree3.ged", encoding='utf-8') as inFile:
        fileLines = [row.strip() for row in inFile]

    idx = []
    names = []
    for l in fileLines:
        k = findID(l)
        n = findName(l)
        if k is not None:
            idx.append(k)
        if n is not None:
            names.append(n)
    data = {ID: Name for ID, Name in zip(idx, names)}
    childPred = []

    it = iter(fileLines)
    while True:
        try:
            line = next(it)
            findFather = re.search(r"1\s+HUSB\s+@I(\d+)@", line)
            if findFather is not None:
                father = data[findFather.group(1)]
                continue

            findMother = re.search(r"1\s+WIFE\s+@I(\d+)@", line)
            if findMother is not None:
                mother = data[findMother.group(1)]
                continue

            findChild = re.search(r"1\s+CHIL\s+@I(\d+)@", line)
            if findChild is not None:
                buf = (data[findChild.group(1)], father, mother)
                childPred.append(buf)
                continue
        except StopIteration:
            break

    printPred = lambda x, y, z: outfile.write("parents(\'{0}\', \'{1}\', \'{2}\').\n".format(x, y, z))
    for count, i in enumerate(childPred):
        child, fath, moth = childPred[count]
        printPred(child, fath, moth)
    outfile.close()