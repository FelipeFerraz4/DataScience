!pip install z3-solver
from z3 import *
from itertools import combinations, product

def printBoard(matriz, numberLine, numberColumn):
  for i in range(0, len(numberLine) * len(numberColumn)):
    if i % len(numberLine) == 0:
      print()
    print(matriz[i], end=" ")

numberLine = [3,0,4,1,3]
numberColumn = [4,1,2,2,2]
barcos = [3,3,2,2,1]
matriz = product(numberLine, numberColumn)
matriz = list(matriz)
printBoard(matriz, numberLine, numberColumn)

propBoard = []
for i in range(0, len(numberLine)):
  for j in range(0, len(numberColumn)):
    propBoard.append(Bool("P" + str(i) + str(j)))

printBoard(propBoard, numberLine, numberColumn)
print("\n")
print(propBoard)

propColumns = []
auxList = []
for adition in range(0, len(numberColumn)):
  for i in range(0, len(numberLine) * len(numberColumn), 5):
    auxList.append(propBoard[i + adition])
  propColumns.append(auxList)
  auxList = []
print(propColumns)

propLines = []
auxList = []
for i in range(0, len(numberLine) * len(numberColumn)):
  if ((i+1) % 5 == 0 and i != 0):
    auxList.append(propBoard[i])
    propLines.append(auxList)
    auxList = []
  else:
    auxList.append(propBoard[i])
print(propLines)

# construindo todas as formulas preposicionais das colunas
#print(propColumns)
psi = []
for i in range(0, len(propColumns)):
  size_prop_True = numberColumn[i]
  size_prop_False = len(numberColumn)-numberColumn[i]

  column_True = combinations(propColumns[i], size_prop_True)
  column_True = list(column_True)
#  print(column_True)
  
  column_False = combinations(propColumns[i], size_prop_False)
  column_False = list(column_False)
#  print(column_False)

#  print()
  phi = []

  for j in range(0, len(column_True)):
    auxList = []
    auxList2 = []


    #print(column_True[j])
    for k in range(0, size_prop_True):
      auxList.append(column_True[j][k])
    auxList = And(auxList)
    #print(auxList)


    #print(column_False[(len(column_False)-1) - j])
    for k in range(0, size_prop_False):
      auxList2.append(Not(column_False[(len(column_False)-1) - j][k]))
    auxList2 = And(auxList2)
    #print(auxList2)

    phi.append(Implies(auxList, auxList2))
    auxList = []
    auxList2 = []

  phi = Or(phi)
  psi.append(phi)
#  print()

psi = And(psi)
print(psi)

# construindo todas as formulas preposicionais das linhas
#print(propLines)
#print()
teta = []
for i in range(0, len(propLines)):
#  print(i)
  size_prop_True = numberLine[i]
  size_prop_False = len(numberLine)-numberLine[i]

  line_True = combinations(propLines[i], size_prop_True)
  line_True = list(line_True)
#  print(line_True)

  line_False = combinations(propLines[i], size_prop_False)
  line_False = list(line_False)
#  print(line_False)

#  print()
  phi = []

  for j in range(0, len(line_True)):
    auxList = []
    auxList2 = []

#    print(line_True[j])
    for k in range(0, size_prop_True):
      auxList.append(line_True[j][k])
    auxList = And(auxList)
#    print(auxList)

#    print(line_False[j])
    for k in range(0, size_prop_False):
      auxList2.append(Not(line_False[(len(line_False)-1) - j][k]))
    auxList2 = And(auxList2)
#    print(auxList2)

    phi.append(Implies(auxList, auxList2))
    auxList = []
    auxList2 = []
#    print()

  phi = Or(phi)
#  print(phi)
#  print()

  teta.append(phi)

teta = And(teta)
print(teta)
