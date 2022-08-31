from typing import List, Dict;
from dataclasses import dataclass;

fileName = './Day11/input.txt';
testFileName = './Day11/testInput.txt';

global nRow, nCol;

@dataclass
class Point:
  rowIdx: int;
  colIdx: int;

def parseFileIntoArray(fileName) -> List[str]:
  # reads into an array
  with open(fileName) as f:
    lines = f.readlines()
  
  sanitizedLines = [line.strip() for line in lines];

  return sanitizedLines;

def parseArrayIntoMatrix(arr: List[str]) -> List[List[int]]:
  matrix = [];
  i = 0;

  for line in arr:
    matrix.append([]);
    for char in line:
      matrix[i].append(int(char));
    i+=1;

  global nRow, nCol;
  nRow = len(matrix);
  nCol = len(matrix[0]) if nRow > 0 else 0;

  return matrix;

# returns None if row/col idx are out of bounds
def increaseEnergy(rowIdx: int, colIdx: int, matrix: List[List[int]]):
  global nRow, nCol;

  if (rowIdx >= 0 and rowIdx < nRow
    and colIdx >= 0 and colIdx < nCol):
    currEnergy = matrix[rowIdx][colIdx];
    return currEnergy + 1;
  else:
    None;

def putPointInDict(i: int, j: int, dict: Dict) -> None:
  if (dict == None):
    print('Dictionary cannot be None');
  if (i not in dict):
    dict[i] = {};
  dict[i][j] = True;

def isInDict(i: int, j: int, dict: Dict) -> bool:
  if (i not in dict):
    return False;
  if (j not in dict[i]):
    return False;
  return True;

def countFlashes(matrix: List[List[int]]) -> int:
  global nRow, nCol;
  nFlashes = 0;

  flashPointsToProcess: List[Point] = [];

  def performUpdatesOnFlash(i, j) -> None:
    nonlocal nFlashes, hasFlashed, flashPointsToProcess;
    nFlashes += 1;
    putPointInDict(i, j, hasFlashed);
    flashPointsToProcess.append(Point(i, j));

  step = 0;
  stepFound = False;
  while not stepFound:
    step += 1;
    # reset hasFlashed
    hasFlashed: Dict = {};

    # increase all octopi energies by 1
    # keep track of which octopi have flashed
    for i in range(nRow):
      for j in range(nCol):
        newEnergy = increaseEnergy(i, j, matrix);
        matrix[i][j] = newEnergy;
        if (newEnergy > 9):
          performUpdatesOnFlash(i, j);

    # process octopi adjacent to flash points
    while (len(flashPointsToProcess) > 0):
      point = flashPointsToProcess.pop();
      rowIdx = point.rowIdx;
      colIdx = point.colIdx;

      # for every combination of -1, +1
      for offsetRow in [-1, 0, 1]:
        for offsetCol in [-1, 0, 1]:
          newEnergy = increaseEnergy(rowIdx+offsetRow, colIdx+offsetCol, matrix);
          if (newEnergy != None):
            matrix[rowIdx+offsetRow][colIdx+offsetCol] = newEnergy;
            if (newEnergy > 9 and not isInDict(rowIdx+offsetRow, colIdx+offsetCol, hasFlashed)):
              performUpdatesOnFlash(rowIdx+offsetRow, colIdx+offsetCol);
    
    stepFlashes = 0;
    # reset energy
    for i in range(nRow):
      for j in range(nCol):
        if (matrix[i][j] > 9):
          stepFlashes += 1;
          matrix[i][j] = 0;
  
    if (stepFlashes == nRow * nCol):
      stepFound = True;

  return nFlashes, step;

def main():
  # inputs = parseFileIntoArray(testFileName);
  inputs = parseFileIntoArray(fileName);
  matrix = parseArrayIntoMatrix(inputs);
  nFlashes, step = countFlashes(matrix);
  print(f'{nFlashes=}', f'{step=}');

main();