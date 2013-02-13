import string

def eingabe():
    matrix = []
    n = int(input("Anzahl Zeilen: "))
    m = int(input("Anzahl Spalten: "))
    for i in range(0, n):
        zeile = []
        for j in range(0, m):
            wert = int(input("a" + str(i+1) + str(j+1) + ": "))
            zeile.append(wert)
        matrix.append(zeile)
    return matrix

def print_matrix(matrix, z):
    for a in range(0, int(z)):
        print (matrix[a])

def print_matrizen(matrizen):
    for m in matrizen:
        print("Matrix " + str(m))
        print_matrix(matrizen[m], len(matrizen[m]))

def transponieren(matrix, n, m):
    trans = []
    for j in range(0, m):
        zeile = []
        for i in range(0, n):
            zeile.append(matrix[i][j])
        trans.append(zeile)
    return trans

def determinante(matrix):
    n = len(matrix)
    m = len(matrix[0])
    if m == n:
        if n == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            print("Determinante: " + str(det))
            return det
        elif n == 3:
            det = matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]+matrix[0][2]*matrix[1][0]*matrix[2][1]-matrix[0][2]*matrix[1][1]*matrix[2][0]-matrix[0][1]*matrix[1][0]*matrix[2][2]-matrix[0][0]*matrix[1][2]*matrix[2][1]
            print("Determinante: " + str(det))
            return det
        else:
            print(".")
    else:
        print("Determinanten können nur von quadratischen Matrizen berechnet werden.")

def addition(matrix1, matrix2):
    n1 = len(matrix1)
    m1 = len(matrix1[0])
    n2 = len(matrix2)
    m2 = len(matrix2[0])
    if n1 == n2 and m1 == m2:
        matrix = []
        for i in range(0, n1):
            zeile = []
            for j in range(0, m1):
                wert = matrix1[i][j] + matrix2[i][j]
                zeile.append(wert)
            matrix.append(zeile)
        print("Ergebnis der Addition:")
        print_matrix(matrix, len(matrix))

def multiplikation(matrix1, matrix2):
    n1 = len(matrix1)
    m1 = len(matrix1[0])
    n2 = len(matrix2)
    m2 = len(matrix2[0])
    if m1 == m2:
        matrix = []
        for i in range(0, n1):
            zeile = []
            for k in range(0, n2):
                wert = 0
                for j in range(0, m1):
                    wert += matrix1[i][j] * matrix2[k][j]
                zeile.append(wert)
            matrix.append(zeile)
        print("Ergebnis der Multiplikation:")
        print_matrix(matrix, len(matrix))        
    else:
        print("falsche Indizes!")

print("Dies ist ein Programm für Matrizenrechnung.")
go = 1

while go == 1:
    anzahl = int(input("Mit wie vielen Matrizen wollen sie Arbeiten? "))

    if anzahl == 1:
        matrix = eingabe()
        print_matrix(matrix, len(matrix))
        determinante(matrix)
        print("Transponierte: ")
        print_matrix(transponieren(matrix, len(matrix), len(matrix[0])), len(matrix[0]))
    elif anzahl > 1:
        matrizen = {}
        k = 0
        for k in range(0, anzahl):
            matrix = eingabe()
            matrizen[k + 1] = matrix
        print_matrizen(matrizen)
        addition(matrizen[1], matrizen[2])
        multiplikation(matrizen[1], transponieren(matrizen[2], len(matrizen[2]), len(matrizen[2][0])))
    mehr = input("Möchten Sie weiter machen? y/n")
    if mehr != "y" and mehr != "Y":
        go = 0



