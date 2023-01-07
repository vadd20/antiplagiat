import ast
import argparse
import os.path


def parsing():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="input")
    parser.add_argument(dest="output")
    args = parser.parse_args()
    return [args.input, args.output]


def loadFromPyFile(file):
    with open(file) as f:
        code = f.read()
    f.close()
    Node = ast.parse(code)
    return ast.dump(Node)


def Levenshtein_distance(a, b):
    str1 = a
    str2 = b
    n, m = len(str1), len(str2)
    matrix = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(n + 1):
        matrix[0][i] = i
    for i in range(m + 1):
        matrix[i][0] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            change = 0 if str1[j - 1] == str2[i - 1] else 1
            first, second, third = matrix[i - 1][j - 1] + change, matrix[i - 1][j] + 1, matrix[i][j - 1] + 1
            matrix[i][j] = min(first, second, third)
    return (max(m, n) - matrix[m][n]) / max(m, n)


def loadFromTxtFile(list1, list2):
    if not os.path.exists(parsing()[0]):
        return print("Text file doesn`t exist")
    with open(parsing()[0]) as f:
        for line in f:
            firstFile, secondFile = line.split()
            list1.append(firstFile)
            list2.append(secondFile)
    f.close()


def saveToFile(list):
    with open(parsing()[1], 'w') as f:
        for i in range(len(changeList)):
            f.write(str(list[i]) + '\n')
    f.close()


if __name__ == "__main__":
    firstListFiles = []
    secondListFiles = []
    scoreList = []
    loadFromTxtFile(firstListFiles, secondListFiles)
    for i in range(len(firstListFiles)):
        scoreList.append(Levenshtein_distance(loadFromPyFile(firstListFiles[i]), loadFromPyFile(secondListFiles[i])))
    saveToFile(scoreList)
